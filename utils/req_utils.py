import requests

def make_request(data_json, type:str='local') -> str:
    # Choose URL
    if type == 'local':
        url = 'http:/127.0.0.1:5001/predict'
    elif type == 'remote':
        url = 'smth/predict'
    # Make request
    response = requests.post(
        url,
        headers = {"content-type": "application/json"},
        data = data_json
        # data='{"Income": 58138, "Recency": 58, "NumWebVisitsMonth": 2, "Complain": 0,"age": 64,"total_purchases": 25,"enrollment_years": 10,"family_size": 1}',
    )
    return response.text