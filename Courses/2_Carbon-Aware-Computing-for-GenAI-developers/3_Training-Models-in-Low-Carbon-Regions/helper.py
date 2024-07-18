import os
from dotenv import load_dotenv
import json
import base64
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials




def authenticate():
    return "DLAI_CEDENTIALS", "silicon-comfort-396606"
    
    #Load .env
    load_dotenv()
    
    #Decode key and store in .JSON
    SERVICE_ACCOUNT_KEY_STRING_B64 = os.getenv('SERVICE_ACCOUNT_KEY')
    SERVICE_ACCOUNT_KEY_BYTES_B64 = SERVICE_ACCOUNT_KEY_STRING_B64.encode("ascii")
    SERVICE_ACCOUNT_KEY_STRING_BYTES = base64.b64decode(SERVICE_ACCOUNT_KEY_BYTES_B64)
    SERVICE_ACCOUNT_KEY_STRING = SERVICE_ACCOUNT_KEY_STRING_BYTES.decode("ascii")

    SERVICE_ACCOUNT_KEY = json.loads(SERVICE_ACCOUNT_KEY_STRING)


    # Create credentials based on key from service account
    # Make sure your account has the roles listed in the Google Cloud Setup section
    credentials = Credentials.from_service_account_info(
        SERVICE_ACCOUNT_KEY,
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    if credentials.expired:
        credentials.refresh(Request())
    
    #Set project ID accoridng to environment variable    
    PROJECT_ID = os.getenv('PROJECT_ID')
    
    #Set staging bucket for training jobs

    return credentials, PROJECT_ID

from dotenv import load_dotenv, find_dotenv 
import os

def load_env():
    _ = load_dotenv(find_dotenv())


def load_emaps_api_key(ret_key=True):
    load_env()
    global api_key
    api_key = os.getenv("ELECTRICITY_MAPS_API_KEY")
    
    if ret_key:
        return api_key
    return
