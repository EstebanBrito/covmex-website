import requests
import os

api_url = os.environ['API_BASE_URL']

def make_request(data_json, type:str='local'):
    # Create URL
    url = f'{api_url}/predict'
    # Make request
    response = requests.post(
        url,
        headers = {"content-type": "application/json"},
        data = data_json # { "SEXO": 0, "EDAD": 56, ... }
    )
    return response.json()