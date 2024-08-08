from api_modules import obtain_data

# API domain name
domain = 'https://api.henrikdev.xyz'

def get_basic_account_details(username: str, tagline: str) -> dict:
    '''
    Retrieves basic data from the specified API URL.

    Parameters:
    - username (str): Username of specified player.
    - tagline (str): Tagline of specified player, cannot contain hashtag.

    Returns:
    - dict: JSON data if the request was successful or an error message if it failed.
    '''
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v1/account/{str(username)}/{str(tagline)}'
    data = obtain_data.obtain_api_data(url)

    return data

def get_detailed_account_details(region: str, puuid: str) -> dict:
    '''
    Retrieves detailed data from the specified API URL.

    Parameters:
    - region (str): Region of specified player.
    - puuid (str): PUUID of specified player, which can be retrieved through getting the basic account details.

    Returns:
    - dict: JSON data if the request was successful or an error message if it failed.
    '''
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v2/by-puuid/mmr/{region}/{puuid}'
    data = obtain_data.obtain_api_data(url)

    return data