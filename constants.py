URL = 'https://api.prizepicks.com/wagers'

# Headers
with open('cookie.txt', 'r') as file:
    COOKIE = file.read().strip()

HEADERS = {
    'cookie': COOKIE,
    'X-Device-Id': 'b4af7e28-2161-41b3-b9e8-5ced47a1fa6b',
    'X-Csrf-Token': '6Ql_L93mXLJtdMGMQ8IYuo8BX7CB4bvRKehuL0IEdRR6i9DzJtfOwC7fLz8NVa0HoIG_N1t805DaiT6I9TxFVQ',
    'X-Device-Info': 'name=,os=mac,osVersion=10.15.7,isSimulator=false,platform=web,appVersion=web',
    'Origin': 'https://app.prizepicks.com',
    'Content-Type': 'application/json',
    'User-Agent': 'PostmanRuntime/7.40.0'
}

PROJECTIONS_COOKIE = "__cf_bm=kXbr30A.rEHytv3LhUm_UC6YkaxFaUL340bP0w05ARE-1721022118-1.0.1.1-tC._y18eHNnk9kt6EOL9DuguojGl0ZUJOe8YTXM9SCq118Titig06Ko2TfZnVnRlro5RqnV7Ox_3P.OjMb33eg; _cfuvid=dnvQyGnmyUvkon_MEL2JOxys8O1zBtmauOhartnWgAg-1721022118548-0.0.1.1-604800000; _pxhd=efd74dca7e43419b404f3332a5522e4af3af2cdb93502d75e9860b26b371f61a:56be1d90-426b-11ef-a2ae-257c9fb4cc07"
SCRAPE_HEADERS = {
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
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

X_API_KEY = "5abbb9e4103cb9a649fe55c7c09398f06a561372"

USER_ID = "78062aa8-a492-4b2c-9afc-decbe1abc0c3"
DEVICE_ID = "051b7f15-1311-46c4-8e7d-f6b6af6dc623"
REQUEST_TYPE = "FORCE"
CHECK_PHASE = "INITIAL"
CLIENT_BRAND = "prizepicksweb"

JURISDICTION_AREA = {
    "id": "usa,tx",
    "name": "USA, TX"
}

SYSTEM_INFO = {
    "platform": "UNKNOWN",
    "jsVersion": "4.4.0"
}

DEVICE_INFO = {
    "brand": "UNKNOWN",
    "model": "UNKNOWN",
    "osVersion": "UNKNOWN"
}

ODDS_API_API_KEY = '2wal0gilwvdTOVnSUkNp'

LEAGUES = ["mlb", "united_states_major_league_soccer"]

DATA_TEMPLATE = '''
{"game_mode":"pickem","new_wager":{"amount_bet_cents":500,"picks":[{"line_score":16.5,"wager_type":"over","projection_id":"2743797","prediction_source":"trending","source_data":""},{"line_score":7.5,"wager_type":"over","projection_id":"2741321","prediction_source":"trending","source_data":""}],"pick_protection":false,"device_library":"js","device_platform":"web","tailed_entry_id":"","is_exact":false},"lat":null,"lng":null,"token":"eyJraWQiOiJwcml6ZXBpY2tzNTc0MHByb2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3hwb2ludC50ZWNoIiwiZGF0YSI6eyJ1c2VySWQiOiI3ODA2MmFhOC1hNDkyLTRiMmMtOWFmYy1kZWNiZTFhYmMwYzMiLCJjbGllbnRJZCI6InByaXplcGlja3M1NzQwcHJvZCIsImRldmljZUlkIjoiMzJhZDU5YTQtMjkwNC00YTZlLTg4ZGMtNGFlZjUyODg0YmI2IiwiaXAiOiIyMDkuMTY2LjEyMi43MSIsInNka1ZlcnNpb24iOiI0LjQuMCIsInJlcXVlc3RJZCI6IjY0ODA0OGM0LTY4Y2EtNDgyYi1iYTE3LTQ0NzMwOGEzYWQyMiIsInN0YXR1cyI6IkFMTE9XRUQiLCJlcnJvcnMiOltdLCJjdXJyZW50Q2hlY2tUeXBlIjoiRk9SQ0UiLCJuZXh0Q2hlY2tJbnRlcnZhbCI6MTAsIm5leHRDaGVja1R5cGUiOiJJTlRFUlZBTCIsImV4cGlyYXRpb25UaW1lIjoxNzIwOTc5MjY3NjkxLCJ0aW1lc3RhbXAiOiIyMDI0LTA3LTE0VDE3OjQ3OjQwLjQ1MVoiLCJjb3VudHJ5IjoiVVNBIiwic3RhdGUiOiJUWCIsImxhdGl0dWRlIjozMC4yNjcyLCJsb25naXR1ZGUiOi05Ny43NDMxLCJkYXRhVHlwZSI6IklQIiwianVyaXNkaWN0aW9uQXJlYSI6eyJpZCI6InVzYSx0eCIsIm5hbWUiOiJVU0EsIFRYIiwiZGV0ZWN0ZWRBdXRvbWF0aWNhbGx5IjpmYWxzZX19LCJleHAiOjE3MjA5NzkyNjcsImlhdCI6MTcyMDk3OTI2MH0.mElDY4HTc4eEPjdY5D1KLWilhtH0p_uke-CVg96V04GX2DIwSLGtV_et98zVk1IFWQU-q59OVVfXmfhX9mOKFDUw_AAd5E045QJ-5S1RnerkthWi2I_9GiXG5KPAmNKZGTj8W-gnCwdN6iuGmhWDxy6khG4V2OdXFdInOvv8BzJfnsADtdWiC2ZCOphfMlthYjaKBr3MgeLEwXvW9gIAeT95mz6i9VqkFhmeY9pHhmDzFxiv4YW2Y_cTZReSJP6eJYiCfGmyllL0hL-SgKWrZBNN_c1ByEIW2OhUJ1c4DDDrB4EVvevmZgTHXBzyQpvyks6tgliyioMz9XJp7sJWQQ","promotion_id":null}
'''