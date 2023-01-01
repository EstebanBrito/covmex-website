import requests

def make_request(data_json, type:str='local'):
    # Choose URL
    if type == 'local':
        url = 'http://0.0.0.0:3000/predict'
    elif type == 'remote':
        url = 'smth/predict'
    # Make request
    response = requests.post(
        url,
        headers = {"content-type": "application/json"},
        data = data_json # { "SEXO": 0, "EDAD": 56, ... }
    )
    return response.json()