import json
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

def clean_input(input:dict) -> dict:
    for key, value in input.keys():
        if value == 'No': input[key] == 0
        if value == 'Sí': input[key] == 1
        if value == 'Hombre': input[key] == 0
        if value == 'Mujer': input[key] == 1
    return input

def predict_mort_pred(input:dict):
    cleaned_input = clean_input(input)
    input_json = json.dumps(cleaned_input)
    response = make_request(input_json)
    # Preprocess response
    return response