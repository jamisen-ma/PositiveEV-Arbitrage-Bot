import pandas as pd
def convert_response_to_csv(data):
    games = data['games']

    # Flattening the JSON structure
    games_df = pd.json_normalize(
        games,
        sep='_',
        record_path=['sportsbooks', 'odds'],
        meta=[
            'id',
            'sport',
            'league',
            ['teams', 'away', 'id'],
            ['teams', 'away', 'name'],
            ['teams', 'away', 'abbreviation'],
            ['teams', 'home', 'id'],
            ['teams', 'home', 'name'],
            ['teams', 'home', 'abbreviation'],
            'start',
            'live',
            ['sportsbooks', 'id'],
            ['sportsbooks', 'name']
        ],
        meta_prefix='meta_',
        errors='ignore'
    )

    return games_df