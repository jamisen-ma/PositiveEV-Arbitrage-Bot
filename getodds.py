import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

pp_props_url = 'https://api.prizepicks.com/projections'
headers = {
'Connection': 'keep-alive',
'Accept': 'application/json; charset=UTF-8',
'User-Agent': 'PostmanRuntime/7.40.0',
'Access-Control-Allow-Credentials': 'true',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Referer': 'https://app.prizepicks.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9'
}

r = requests.get(pp_props_url, headers=headers, verify=False)
print(r)
df = pd.json_normalize(r.json()['data'])
df.to_csv("sample_projections.csv")
print(df.columns)