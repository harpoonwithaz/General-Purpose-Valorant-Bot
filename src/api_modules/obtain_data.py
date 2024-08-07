import requests
from dotenv import load_dotenv
import os

def obtain_api_data(url: str):
    '''
    Returns
    - Json data if the request was successful
    - Error message containing the reason the request failed
    '''
    # Load environment variables from .env file
    load_dotenv()

    # Access the API key
    api_key = os.getenv('API_KEY')

    # Set up the headers, including the authorization header with the API key
    headers = {
        "accept": "application/json",
        "Authorization": str(api_key)
    }

    # Sends a GET request to the specified API url
    response = requests.get(url, headers=headers)

    # Checks if the response was valid
    if response.status_code == 200:
        json_data = response.json()
        error_message = None
    else:
        # Prints out error message from API
        error_message = (response.json()['errors'][0]['message'])
        json_data = None

    return json_data, error_message