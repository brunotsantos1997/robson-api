import json

import requests

from .app import CLIENT_ID, CLIENT_SECRET
from .constants import XP_TOKEN_API



def get_xp_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Host': 'openapi.xpi.com.br',
        'User-Agent': 'Robson/0.1',
    }
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response_content = json.loads(requests.post(XP_TOKEN_API, headers=headers, data=data).content)
    token = response_content['access_token']
    return token
