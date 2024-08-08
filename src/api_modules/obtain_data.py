import requests
from dotenv import load_dotenv
import os

def obtain_api_data(url: str, use_headers: bool = True) -> dict:
    '''
    Retrieves data from the specified API URL.

    Parameters:
    - url (str): The API endpoint to request data from.
    - use_headers (bool): Whether to include default headers with the request.

    Returns:
    - dict: JSON data if the request was successful or an error message if it failed.
    '''

    # Load environment variables from .env file
    load_dotenv()

    # Access the API key
    api_key = os.getenv('API_KEY')
    if not api_key:
        return {'error': 'API key not found in environment variables'}

    # Set up the headers, including the authorization header with the API key
    default_headers = {
        "accept": "application/json",
        "Authorization": str(api_key)
    }

    try:
        # If specified, will send request to API with headers containing API key
        if use_headers:
            # Sends a GET request to the specified API url with headers
            response = requests.get(url, headers=default_headers)
        else:
            # Sends a GET request to the specified API url
            response = requests.get(url)

        # Checks if the response was valid
        if response.ok:
            return response.json()
        # Request error by the client (missing query for example)
        elif response.status_code == 400:
            return {'error': f'{response.json()['errors'][0]['message']}'}
        # Unauthorized access
        elif response.status_code == 401:
            return {'error': 'Unauthorized access'}
        # Forbidden to connect to the Riot API (mainly maintenance reasons on riot side like patches) or to the HenrikDev API itself because of bot prevention for example
        elif response.status_code == 403:
            return {'error': 'Forbidden access'}
        # The entity was not found (player/match/general data)
        elif response.status_code == 404:
            return {'error': f'{response.json()['errors'][0]['message']}'}
        # Timeout while fetching riot data
        elif response.status_code == 408:
            return {'error': 'Timeout while fetching riot data'}
        # Rate limit reached (can be global API limit which affects all users or just you, when the "x-ratelimit-remaining" header is 0 then it's a personal limit)
        elif response.status_code == 429:
            return {'error': f'{response.json()['errors'][0]['message']}'}
        # Riot API seems to be down, API unable to connect
        elif response.status_code == 503:
            return {'error': f'{response.json()['errors'][0]['message']}'}
        # Other errors
        else:
            return {'error': f'{response.json()['errors'][0]['message']}'}
    
    except requests.exceptions.RequestException as e:
        return {'error': f'Request failed: {str(e)}'}