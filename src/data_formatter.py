# Imports valorant API request module
from api_modules import valorant_api

def get_player_info(name: str, tag: str) -> dict:
    # Makes request to API and returns json data and error message if any
    basic_data, error_message = valorant_api.get_basic_account_details(name, tag)

    # Checks if nothing was returned from the API
    if basic_data != None:
        # Makes request to API with PUUID to get detailed player data
        detailed_data, error_message = valorant_api.get_detailed_account_details(basic_data['data']['region'], basic_data['data']['puuid'])
        
        # Checks if nothing was returned from the API
        if detailed_data != None:
            # Organizes JSON data from API into dictionary
            player_data = {
                'username': detailed_data['data']['name'],
                'tagline': detailed_data['data']['tag'],
                'PUUID': basic_data['data']['puuid'],
                'region': basic_data['data']['region'],
                'level': basic_data['data']['account_level'],
                'banner_small': basic_data['data']['card']['small'],
                'banner_large': basic_data['data']['card']['large'],
                'banner_wide': basic_data['data']['card']['wide'],
                'current_rank': detailed_data['data']['current_data']['currenttierpatched'],
                'current_rank_tier': detailed_data['data']['current_data']['currenttierpatched']
            }
    else:
        print('Error: ', error_message  )
    
# This is a comment
get_player_info('H00DBYAIR', 'BMWM5')