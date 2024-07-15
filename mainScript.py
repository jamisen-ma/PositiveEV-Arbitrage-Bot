from data_cleaning import *
from getodds import *
from controller import *

for league in LEAGUES:
    all_odds = []  # List to hold all DataFrames

    sportsbooks = get_sportsbooks()
    for sportsbook in sportsbooks:
        odds_data = get_odds(league, sportsbook)
        all_odds.append(convert_response_to_csv(odds_data))

    # Concatenate all DataFrames and save to CSV
    if all_odds:
        print(all_odds)
        df = pd.concat(all_odds, ignore_index=True)
        filename = f"{league}.csv"
        df['sportsbook'] = df['id'].apply(lambda x: x.split(':')[0])
        df['bet'] = df['id'].apply(lambda x: ':'.join(x.split(':')[1:]))

        # Combine market and name into one column
        df['market_name'] = df['market'] + ': ' + df['name']

        # Drop the original id, market, and name columns
        df.drop(columns=['id', 'market', 'name'], inplace=True)

        # Reorder columns to place market_name, odds, and meta_sportsbooks_id as the first three columns
        cols = df.columns.tolist()
        cols = ['market_name', 'price', 'meta_sportsbooks_id'] + [col for col in cols if
                                                                  col not in ['market_name', 'price',
                                                                              'meta_sportsbooks_id']]
        df = df[cols]

        # Sort by bet
        df_sorted = df.sort_values(by='bet')

        df_sorted.to_csv(filename, index=False)
        print(f"Data for {league} saved to {filename}")