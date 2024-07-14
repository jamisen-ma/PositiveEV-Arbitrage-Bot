URL = 'https://api.prizepicks.com/wagers'

# Headers
with open('cookie.txt', 'r') as file:
    cookie = file.read().strip()

HEADERS = {
    'cookie': cookie,
    'X-Device-Id': 'b4af7e28-2161-41b3-b9e8-5ced47a1fa6b',
    'X-Csrf-Token': '6Ql_L93mXLJtdMGMQ8IYuo8BX7CB4bvRKehuL0IEdRR6i9DzJtfOwC7fLz8NVa0HoIG_N1t805DaiT6I9TxFVQ',
    'X-Device-Info': 'name=,os=mac,osVersion=10.15.7,isSimulator=false,platform=web,appVersion=web',
    'Origin': 'https://app.prizepicks.com',
    'Content-Type': 'application/json'
}

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

