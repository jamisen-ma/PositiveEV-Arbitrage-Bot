import pandas as pd
from itertools import combinations
def positive_ev(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Function to convert odds to a common comparable value (implied probability)

    # Function to detect if a bet has 15% better odds than the average of other bets

    # Detect bets with better odds
    better_odds_bets = detect_better_odds(df)

    # Print the results
    if better_odds_bets:
        print("Bets with 15% better odds than the average of the other bets in their market:")
        for market_name, price, avg_price, current_probability, avg_probability, sportsbook in better_odds_bets:
            print(
                f"Market: {market_name}, Price: {price}, Average Price: {avg_price}, Current Probability: {current_probability:.2%}, Average Probability: {avg_probability:.2%}, Sportsbook: {sportsbook}")
    else:
        print("No bets found with 15% better odds than the average of the other bets in their market.")


def odds_to_probability(odds):
    if odds < 0:
        return -odds / (-odds + 100)
    else:
        return 100 / (odds + 100)import pandas as pd
def positive_ev(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Function to convert odds to a common comparable value (implied probability)

    # Function to detect if a bet has 15% better odds than the average of other bets

    # Detect bets with better odds
    better_odds_bets = detect_better_odds(df)

    # Print the results
    if better_odds_bets:
        print("Bets with 15% better odds than the average of the other bets in their market:")
        for market_name, price, avg_price, current_probability, avg_probability, sportsbook in better_odds_bets:
            print(
                f"Market: {market_name}, Price: {price}, Average Price: {avg_price}, Current Probability: {current_probability:.2%}, Average Probability: {avg_probability:.2%}, Sportsbook: {sportsbook}")
    else:
        print("No bets found with 15% better odds than the average of the other bets in their market.")


def odds_to_probability(odds):
    if odds < 0:
        return -odds / (-odds + 100)
    else:
        return 100 / (odds + 100)

def detect_better_odds(df):
    result = []

    # Iterate over each unique market_name
    for market_name, group in df.groupby('market_name'):
        if len(group) >= 3:
            for index, row in group.iterrows():
                # Exclude the current row and calculate the average price of other bets
                other_prices = group.loc[group.index != index, 'price']
                if not other_prices.empty:
                    avg_price = other_prices.mean()
                    # Calculate the implied probability of the current price and the average price
                    current_probability = odds_to_probability(row['price'])
                    avg_probability = other_prices.apply(odds_to_probability).mean()
                    # Check if the current price is 15% better than the average (lower implied probability is better)
                    if current_probability < avg_probability * 0.85:
                        result.append((market_name, row['price'], avg_price, current_probability, avg_probability,
                                       row['sportsbook']))
    return result

def detect_better_odds(df):
    result = []

    # Iterate over each unique market_name
    for market_name, group in df.groupby('market_name'):
        if len(group) >= 3:
            for index, row in group.iterrows():
                # Exclude the current row and calculate the average price of other bets
                other_prices = group.loc[group.index != index, 'price']
                if not other_prices.empty:
                    avg_price = other_prices.mean()
                    # Calculate the implied probability of the current price and the average price
                    current_probability = odds_to_probability(row['price'])
                    avg_probability = other_prices.apply(odds_to_probability).mean()
                    # Check if the current price is 15% better than the average (lower implied probability is better)
                    if current_probability < avg_probability * 0.85:
                        result.append((market_name, row['price'], avg_price, current_probability, avg_probability,
                                       row['sportsbook']))
    return result


def detect_arbitrage_opportunities(df):
    opportunities = []

    # Iterate over each unique market_name
    for market_name, group in df.groupby('market_name'):
        # Calculate the implied probability for each bet
        group['implied_probability'] = group['price'].apply(odds_to_probability)

        # Find combinations of bets that cover all outcomes
        for combo in combinations(group.index, 2):
            prob_sum = group.loc[combo, 'implied_probability'].sum()
            if prob_sum < 1:
                opportunities.append({
                    'market_name': market_name,
                    'bets': group.loc[combo].to_dict(orient='records'),
                    'total_implied_probability': prob_sum
                })

    return opportunities