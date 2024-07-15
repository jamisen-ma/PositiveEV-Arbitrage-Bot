import requests
from constants import *
def get_sportsbooks():
    url = f'https://api.oddsblaze.com/v1/sportsbooks?key={ODDS_API_API_KEY}&=null'
    response = requests.get(url)
    sportsbooks_data = response.json()
    ids = [sportsbook['id'] for sportsbook in sportsbooks_data.get('sportsbooks', [])]
    return ids
def get_odds(league, book):
    url = f'https://api.oddsblaze.com/v1/odds?key={ODDS_API_API_KEY}&league={league}&sportsbook={book}'
    response = requests.get(url)
    print(f'Recevied {league} data from {book}')
    print(response.json())
    return response.json()

