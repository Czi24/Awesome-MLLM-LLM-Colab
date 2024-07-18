from google.oauth2.service_account import Credentials

from dotenv import load_dotenv, find_dotenv 
import os

def authenticate():
    return "DLAI_CREDENTIALS", "silicon-comfort-396606"

def load_env():
    _ = load_dotenv(find_dotenv())


def load_emaps_api_key(ret_key=True):
    load_env()
    global api_key
    api_key = os.getenv("ELECTRICITY_MAPS_API_KEY")
    
    if ret_key:
        return api_key
    return
