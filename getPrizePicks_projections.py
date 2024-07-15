import requests
import pandas as pd
import json


def getPrizePicksProjectionsService():
    # Define the API URL
    url = 'https://api.prizepicks.com/projections'

    # Define the headers
    headers = {
        'Cookie': '__cf_bm=kXbr30A.rEHytv3LhUm_UC6YkaxFaUL340bP0w05ARE-1721022118-1.0.1.1-tC._y18eHNnk9kt6EOL9DuguojGl0ZUJOe8YTXM9SCq118Titig06Ko2TfZnVnRlro5RqnV7Ox_3P.OjMb33eg; _cfuvid=dnvQyGnmyUvkon_MEL2JOxys8O1zBtmauOhartnWgAg-1721022118548-0.0.1.1-604800000; _pxhd=efd74dca7e43419b404f3332a5522e4af3af2cdb93502d75e9860b26b371f61a:56be1d90-426b-11ef-a2ae-257c9fb4cc07',
        'User-Agent': 'PostmanRuntime/7.40.0'
    }

    # Fetch the data from the API with SSL verification disabled
    response = requests.get(url, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

    # Load the JSON data
    data = response.json()

    # Extract projections and players data
    projections = data['data']
    players = data['included']

    # Create DataFrame for projections
    projections_df = pd.json_normalize(projections, sep='_')
    projections_df = projections_df[
        ['id', 'attributes_line_score', 'attributes_stat_type', 'relationships_new_player_data_id',
         'relationships_league_data_id']]
    projections_df.columns = ['projection_id', 'line_score', 'stat_type', 'player_id', 'league_id']

    # Create DataFrame for players
    players_df = pd.json_normalize(players, sep='_')
    players_df = players_df[['id', 'attributes_display_name', 'attributes_league']]
    players_df.columns = ['player_id', 'player_name', 'league']

    # Merge DataFrames on player_id
    merged_df = pd.merge(projections_df, players_df, on='player_id')

    # Reorder columns as required
    final_df = merged_df[['player_name', 'projection_id', 'line_score', 'stat_type', 'league']]

    # Sort the DataFrame by league and then by stat_type
    final_df_sorted = final_df.sort_values(by=['league', 'stat_type'])

    return final_df_sorted


# Call the method and get the DataFrame
final_df = getPrizePicksProjectionsService()
final_df.to_csv("PrizePicks_projections.csv", index=False)
# Display the resulting DataFrame
print(final_df)
