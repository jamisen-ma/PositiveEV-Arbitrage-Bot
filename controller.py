import json

from util import *
import requests
from flask import Flask, jsonify
from constants import *
import uuid
app = Flask(__name__)

@app.route('/verify_location', methods=['GET'])
def verify_location(token):
    # Make the request to the PrizePicks API
    url = f'https://api.prizepicks.com/geo/verify_location?token={token}'
    response = requests.get(url)

    # Return the response from the PrizePicks API
    return jsonify(response.json()), response.status_code
def place_wager(data):
    # Read the cookie from the file
    with open("cookie.txt", 'r') as file:
        cookie = file.read().strip()

    # Update the headers with the cookie
    headers = HEADERS.copy()
    headers['Cookie'] = cookie

    # Update the data template with the token

    response = requests.post(URL, headers=headers, json=data)

    return response.json()


def init_force(requestID):
    url = 'https://oregon-xp26.xpoint.tech/init-force'
    headers = {
        'x-api-key': X_API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        "clientInfo": {
            "userId": USER_ID,
            "deviceId": DEVICE_ID,
            "requestType": REQUEST_TYPE,
            "checkPhase": CHECK_PHASE,
            "clientBrand": CLIENT_BRAND,
            "jurisdictionArea": JURISDICTION_AREA,
            "systemInfo": SYSTEM_INFO,
            "deviceInfo": DEVICE_INFO,
            "requestId": requestID,
            "initialRequestId": requestID
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()

    return response_data.get("jobId"), requestID


def force_result(jobID, requestID):
    url = 'https://oregon-xp26.xpoint.tech/force-result'
    headers = {
        'Host': 'oregon-xp26.xpoint.tech',
        'x-api-key': X_API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        "jobId": jobID,
        "clientInfo": {
            "userId": USER_ID,
            "deviceId": DEVICE_ID,
            "requestType": REQUEST_TYPE,
            "checkPhase": CHECK_PHASE,
            "clientBrand": CLIENT_BRAND,
            "jurisdictionArea": JURISDICTION_AREA,
            "systemInfo": SYSTEM_INFO,
            "deviceInfo": DEVICE_INFO,
            "requestId": requestID,
            "initialRequestId": requestID
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    xpoint_jwt = response.headers.get("xpoint-jwt")

    return xpoint_jwt


def ping_api():
    url = 'https://oregon-xp26.xpoint.tech/pingapi'
    headers = {
        'x-api-key': X_API_KEY,
        'Content-Type': 'application/json'
    }
    request_id = str(uuid.uuid4())
    data = {
        "clientInfo": {
            "userId": "ping",
            "deviceId": "32ad59a4-2904-4a6e-88dc-4aef52884bb6",
            "requestType": REQUEST_TYPE,
            "checkPhase": CHECK_PHASE,
            "systemInfo": {
                "platform": "UNKNOWN",
                "jsVersion": "4.4.0"
            },
            "deviceInfo": {
                "brand": "UNKNOWN",
                "model": "UNKNOWN",
                "osVersion": "UNKNOWN"
            },
            "requestId": request_id
        }
    }
    requests.post(url, headers=headers, data=json.dumps(data))
    return request_id


def gps():
    url = 'https://oregon-xp26.xpoint.tech/gps'
    headers = {
        'x-api-key': X_API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        "systemInfo": SYSTEM_INFO,
        "idType": "UNKNOWN",
        "rows": [
            {
                "accuracy": 14.612,
                "timestamp": 1720937584448,
                "latitudeE6": 30290627,
                "longitudeE6": -97750273,
                "adId": "unknown",
                "provider": "xpoint-lite"
            }
        ],
        "userKey": {
            "userId": USER_ID,
            "deviceId": DEVICE_ID,
            "clientBrand": CLIENT_BRAND,
            "jurisdictionArea": JURISDICTION_AREA
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))


def wagers(xpointjwt, wager_payload):
    url = 'https://api.prizepicks.com/wagers'
    headers = HEADERS
    headers['xpoint-jwt'] = xpointjwt

    # data = {
    #     "game_mode": "pickem",
    #     "new_wager": {
    #         "amount_bet_cents": 500,
    #         "picks": [
    #             {
    #                 "line_score": 16.5,
    #                 "wager_type": "over",
    #                 "projection_id": "2743797",
    #                 "prediction_source": "trending",
    #                 "source_data": ""
    #             },
    #             {
    #                 "line_score": 7.5,
    #                 "wager_type": "over",
    #                 "projection_id": "2741321",
    #                 "prediction_source": "trending",
    #                 "source_data": ""
    #             }
    #         ],
    #         "pick_protection": False,
    #         "device_library": "js",
    #         "device_platform": "web",
    #         "tailed_entry_id": "",
    #         "is_exact": False
    #     },
    #     "lat": None,
    #     "lng": None,
    #     "token": xpointjwt,
    #     "promotion_id": None
    # }

    response = requests.post(url, headers=headers, data=json.dumps(wager_payload))



