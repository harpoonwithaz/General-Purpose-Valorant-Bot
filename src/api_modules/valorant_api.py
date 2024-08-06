from api_modules import obtain_data

# API domain name
domain = 'https://api.henrikdev.xyz'

def get_basic_account_details(username: str, tagline: str):
    '''
    Returns:
    - data,
    Json data containing player info from the API
    - error_message,
    If there is any error message from the API, it will be included, otherwise it will say None
    '''
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v1/account/{str(username)}/{str(tagline)}'
    data, error_message = obtain_data.obtain_api_data(url)

    return data, error_message

def get_detailed_account_details(region: str, puuid: str):
    '''
    Returns:
    - data
    Json data containing player info from the API
    - error_message
    If there is any error message from the API, it will be included, otherwise it will say None
    '''
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v2/by-puuid/mmr/{region}/{puuid}'
    data, error_message = obtain_data.obtain_api_data(url)

    return data, error_message
def get_Ranked_Icon(tier)
    #this pulls the ranked icon's from the API URL
    url ={}https://valorant-api.com/v1/competitivetiers