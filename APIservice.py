from flask import Flask, request, jsonify
import pandas as pd
from data_cleaning import *
from getodds import *
from controller import *
from getPrizePicks_projections import *
from positiveEVfinder import *
app = Flask(__name__)

# Define your API key (in a real application, store this securely)
VALID_API_KEY = "your_secure_api_key"


@app.route('/getSportsBooksOdds', methods=['GET'])
def getSportsBooksOdds():
    api_key = request.args.get('api_key')
    sport = request.args.get('sport')

    # Check if the API key is provided and valid
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403

    # Check if the sport parameter is provided
    if not sport:
        return jsonify({"error": "Sport parameter is required"}), 400

    all_odds = []

    sportsbooks = get_sportsbooks()
    for sportsbook in sportsbooks:
        odds_data = get_odds(sport, sportsbook)
        all_odds.append(convert_response_to_csv(odds_data))

    if all_odds:
        df = pd.concat(all_odds, ignore_index=True)
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

        # Convert to JSON and return
        return df_sorted.to_json(orient='records'), 200
    else:
        return jsonify({"error": "No odds data found for the specified sport"}), 404

@app.route('/getPrizePicksProjections', methods=['GET'])
def getPrizePicksProjections():
    # Get the API key from the request
    api_key = request.args.get('api_key')
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403

    # Get optional filters from the request
    league_filter = request.args.get('league')
    stat_type_filter = request.args.get('stat_type')
    player_filter = request.args.get('player')

    # Get the projections data
    projections = getPrizePicksProjectionsService()

    # Apply filters if provided
    if league_filter:
        projections = projections[projections['league'] == league_filter]
    if stat_type_filter:
        projections = projections[projections['stat_type'] == stat_type_filter]
    if player_filter:
        projections = projections[projections['player_name'].str.contains(player_filter, case=False)]

    # Convert the DataFrame to JSON
    result = projections.to_json(orient='records')

    return result, 200

@app.route('/positiveEVFinder', methods=['GET'])
def positiveEVFinder():
    api_key = request.args.get('api_key')
    data = request.args.get('data')
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403
    result = positive_ev(data).to_json(orient='records')
    return result

@app.route('/arbitrageFinder', methods=['GET'])
def arbitrageFinder():
    api_key = request.args.get('api_key')
    data = request.args.get('data')
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403
    result = positive_ev(data).to_json(orient='records')
    return result

@app.route('/placePrizePicksWager', methods=['POST'])
def placePrizePicksWager():
    api_key = request.args.get('api_key')
    wager_info = request.args.get('wager_info')
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403
    place_wager(wager_info)
    return jsonify({"success": True}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
