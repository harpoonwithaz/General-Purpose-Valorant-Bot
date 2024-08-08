# Imports valorant API request module
from api_modules import valorant_api

def get_player_info(name: str, tag: str) -> dict:
    # Makes request to API and returns json data and error message if any
    basic_data = valorant_api.get_basic_account_details(name, tag)

    if 'error' in basic_data:
        print(f"Error: {basic_data['error']}")
        return basic_data
    
    # Process the JSON data if the request was successful
    try:
        # Assume the API returns a dictionary with a 'results' key
        results = data.get('results', [])
        if not results:
            print("No data available.")
            return

        # Process each result (example)
        for item in results:
            print(f"Item: {item['name']}, Value: {item['value']}")

    except KeyError as e:
        print(f"Data format error: missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing data: {e}")

    '''# Checks if nothing was returned from the API
    if basic_data != None:
        # Makes request to API with PUUID to get detailed player data
        detailed_data = valorant_api.get_detailed_account_details(basic_data['data']['region'], basic_data['data']['puuid'])
        
        # Checks if nothing was returned from the API
        if detailed_data != None:
            # Gets players ranked stats and stores in variable
            ranked_stats = detailed_data['data']['by_season']

            # Variable to store the total wins
            total_wins = 0
            total_games = 0

            # Iterate over the outer dictionary
            for outer_key, inner_dict in ranked_stats.items():
                # Check if 'error' is not a key in the inner dictionary
                if 'error' not in inner_dict:
                    # Add the wins to the total
                    total_wins += int(inner_dict.get('wins', 0))
                    total_games += int(inner_dict.get('number_of_games', 0))

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
                'current_rank_tier': detailed_data['data']['current_data']['currenttier'],
                'current_rank_icons': detailed_data['data']['current_data']['images'],
                'all_time_ranked_wins': total_wins,
                'all_time_ranked_games': total_games,
                'all_time_ranked_loses': total_games - total_wins,
                'all_time_winrate': int((total_wins / total_games) * 100),
                'peak_rank': detailed_data['data']['highest_rank']['patched_tier'],
                'peak_rank_tier': detailed_data['data']['highest_rank']['tier'],
            }
            return player_data
    else:
        print('Error:', error_message)
        return {
            'error': error_message
        }
'''
# TESTING VARIABLES
# Username: SEN TenZ
# Tagline: 81619

# Username: BESTVALORANTNERD
# Tagline SHELL

data = get_player_info('SEN TenZ', 'uhsaduashd')

print(data)