import os
from typing import List, Optional
from pydantic import BaseModel, ValidationError
from datetime import datetime
import pandas as pd
import openai
from pymongo.collection import Collection
from pymongo.errors import OperationFailure
from pymongo.operations import SearchIndexModel
from pymongo.mongo_client import MongoClient
import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

DB_NAME = "airbnb_dataset"
COLLECTION_NAME = "listings_reviews"

class Host(BaseModel):
    host_id: str
    host_url: str
    host_name: str
    host_location: str
    host_about: str
    host_response_time: Optional[str] = None
    host_thumbnail_url: str
    host_picture_url: str
    host_response_rate: Optional[int] = None
    host_is_superhost: bool
    host_has_profile_pic: bool
    host_identity_verified: bool

class Location(BaseModel):
    type: str
    coordinates: List[float]
    is_location_exact: bool

class Address(BaseModel):
    street: str
    government_area: str
    market: str
    country: str
    country_code: str
    location: Location

class Review(BaseModel):
    _id: str
    date: Optional[datetime] = None
    listing_id: str
    reviewer_id: str
    reviewer_name: Optional[str] = None
    comments: Optional[str] = None

class Listing(BaseModel):
    _id: int
    listing_url: str
    name: str
    summary: str
    space: str
    description: str
    neighborhood_overview: Optional[str] = None
    notes: Optional[str] = None
    transit: Optional[str] = None
    access: str
    interaction: Optional[str] = None
    house_rules: str
    property_type: str
    room_type: str
    bed_type: str
    minimum_nights: int
    maximum_nights: int
    cancellation_policy: str
    last_scraped: Optional[datetime] = None
    calendar_last_scraped: Optional[datetime] = None
    first_review: Optional[datetime] = None
    last_review: Optional[datetime] = None
    accommodates: int
    bedrooms: Optional[float] = 0
    beds: Optional[float] = 0
    number_of_reviews: int
    bathrooms: Optional[float] = 0
    amenities: List[str]
    price: int
    security_deposit: Optional[float] = None
    cleaning_fee: Optional[float] = None
    extra_people: int
    guests_included: int
    images: dict
    host: Host
    address: Address
    availability: dict
    review_scores: dict
    reviews: List[Review]
    text_embeddings: List[float]

def process_records(data_frame):
    records = data_frame.to_dict(orient='records')
    # Handle potential `NaT` values
    for record in records:
        for key, value in record.items():
            # Check if the value is list-like; if so, process each element.
            if isinstance(value, list):
                processed_list = [None if pd.isnull(v) else v for v in value]
                record[key] = processed_list
            # For scalar values, continue as before.
            else:
                if pd.isnull(value):
                    record[key] = None
    try:
        # Convert each dictionary to a Listing instance
        listings = [Listing(**record).dict() for record in records]
        return listings
    except ValidationError as e:
        print("Validation error:", e)
        return []
    


def get_embedding(text):
    """Generate an embedding for the given text using OpenAI's API."""

    # Check for valid input
    if not text or not isinstance(text, str):
        return None

    try:
        # Call OpenAI API to get the embedding
        embedding = openai.embeddings.create(
            input=text,
            model="text-embedding-3-small", dimensions=1536).data[0].embedding
        return embedding
    except Exception as e:
        print(f"Error in get_embedding: {e}")
        return None
    

def setup_vector_search_index(collection: Collection, 
                              text_embedding_field_name: str = "text_embeddings", 
                              vector_search_index_name: str = "vector_index_text"):
    """
    Sets up a vector search index for a MongoDB collection based on text embeddings.

    Parameters:
    - collection (Collection): The MongoDB collection to which the index is applied.
    - text_embedding_field_name (str): The field in the documents that contains the text embeddings.
    - vector_search_index_name (str): The name for the vector search index.

    Returns:
    - None
    """
    # Define the model for the vector search index
    vector_search_index_model = SearchIndexModel(
        definition={
            "mappings": { # describes how fields in the database documents are indexed and stored
                "dynamic": True, # automatically index new fields that appear in the document
                "fields": { # properties of the fields that will be indexed.
                    text_embedding_field_name: { 
                        "dimensions": 1536, # size of the vector.
                        "similarity": "cosine", # algorithm used to compute the similarity between vectors
                        "type": "knnVector",
                    }
                },
            }
        },
        name=vector_search_index_name, # identifier for the vector search index
    )

    # Check if the index already exists
    index_exists = False
    for index in collection.list_indexes():
        if index['name'] == vector_search_index_name:
            index_exists = True
            break

    # Create the index if it doesn't exist
    if not index_exists:
        try:
            result = collection.create_search_index(vector_search_index_model)
            print("Creating index...")
            time.sleep(20)  # Sleep for 20 seconds, adding sleep to ensure vector index has compeleted inital sync before utilization
            print(f"Index created successfully: {result}")
            print("Wait a few minutes before conducting search with index to ensure index initialization.")
        except OperationFailure as e:
            print(f"Error creating vector search index: {str(e)}")
    else:
        print(f"Index '{vector_search_index_name}' already exists.")


def vector_search_with_filter(user_query, db, collection, additional_stages=[], vector_index="vector_index_text"):
    """
    Perform a vector search in the MongoDB collection based on the user query.

    Args:
    user_query (str): The user's query string.
    db (MongoClient.database): The database object.
    collection (MongoCollection): The MongoDB collection to search.
    additional_stages (list): Additional aggregation stages to include in the pipeline.

    Returns:
    list: A list of matching documents.
    """

    # Generate embedding for the user query
    query_embedding = get_embedding(user_query)

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search stage
    vector_search_stage = {
        "$vectorSearch": {
            "index": vector_index,  # specifies the index to use for the search
            "queryVector": query_embedding,  # the vector representing the query
            "path": "text_embeddings",  # field in the documents containing the vectors to search against
            "numCandidates": 150,  # number of candidate matches to consider
            "limit": 20,  # return top 20 matches
            "filter": {
                "$and": [
                    {"accommodates": {"$gte": 2}}, 
                    {"bedrooms": {"$lte": 7}}
                ]
            },
        }
    }


    # Define the aggregate pipeline with the vector search stage and additional stages
    pipeline = [vector_search_stage] + additional_stages

    # Execute the search
    results = collection.aggregate(pipeline)

    explain_query_execution = db.command( # sends a database command directly to the MongoDB server
        'explain', { # return information about how MongoDB executes a query or command without actually running it
            'aggregate': collection.name, # specifies the name of the collection on which the aggregation is performed
            'pipeline': pipeline, # the aggregation pipeline to analyze
            'cursor': {} # indicates that default cursor behavior should be used
        }, 
        verbosity='executionStats') # detailed statistics about the execution of each stage of the aggregation pipeline

    vector_search_explain = explain_query_execution['stages'][0]['$vectorSearch']
    millis_elapsed = vector_search_explain['explain']['collectStats']['millisElapsed']

    print(f"Total time for the execution to complete on the database server: {millis_elapsed} milliseconds")

    return list(results)




def connect_to_database():
    """Establish connection to the MongoDB."""

    MONGO_URI = os.environ.get("MONGO_URI")

    if not MONGO_URI:
        print("MONGO_URI not set in environment variables")

    # gateway to interacting with a MongoDB database cluster
    mongo_client = MongoClient(MONGO_URI, appname="devrel.deeplearningai.python")
    print("Connection to MongoDB successful")

    # Pymongo client of database and collection
    db = mongo_client.get_database(DB_NAME)
    collection = db.get_collection(COLLECTION_NAME)

    return db, collection