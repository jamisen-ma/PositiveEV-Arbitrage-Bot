import requests
import pandas as pd
from http.cookiejar import CookieJar


def get_projections(cookie_file_path):
    # Read the cookie from the file
    with open(cookie_file_path, 'r') as file:
        cookie_value = file.read().strip()

    # Create a session
    session = requests.Session()

    # Set the initial headers
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'If-Modified-Since': 'Sun, 14 Jul 2024 01:04:49 GMT',
        'Priority': 'u=0, i',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    # Set the cookie
    session.cookies.set('Cookie', cookie_value, domain='.prizepicks.com')

    # Make the request
    pp_props_url = 'https://api.prizepicks.com/projections?league_id=163&per_page=250&single_stat=true'

    try:
        response = session.get(pp_props_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        response_json = response.json()

        # Normalize the JSON response to a DataFrame
        df = pd.json_normalize(response_json, record_path=['data'])

        # Save DataFrame to CSV
        df.to_csv('player_props_20221030.csv', index=False)

        print("Data has been successfully saved to player_props_20221030.csv")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
        print(f"Response content: {response.content}")  # Print the response content
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


# Example usage:
cookie_file_path = "cookie.txt"
get_projections(cookie_file_path)
