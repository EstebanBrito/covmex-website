import json
from .req_utils import make_request
import random

def map_value(value:any) -> int:
    # Map YES/NO inputs
    if value == 'No': return 0
    if value == 'Sí': return 1
    # MAP sex
    if value == 'Hombre': return 0
    if value == 'Mujer': return 1
    # If mapping does not apply, return original value
    return value

def clean_input(input:dict) -> dict:
    for key, value in input.items():
        input[key] = map_value(value)
    return input

def predict_mort_pred(input:dict, mocked:bool=True):
    # Preprocess input
    cleaned_input = clean_input(input)
    input_json = json.dumps(cleaned_input)
    # Make request, get response
    if mocked: response_json = { 'prediction': random.random() }
    else: response_json = make_request(input_json, type='remote')
    # Preprocess response
    prediction = response_json['prediction']
    return prediction

def get_prediction_info(prediction):
    if prediction > 0.66:
        clfn = 'High Risk'
        clfn_color = f':red[{clfn}]'
        advice = 'High risk of death. It is imperative to go to the hospital.'
    elif prediction > 0.33:
        clfn = 'Medium Risk'
        clfn_color = f':orange[{clfn}]'
        advice = 'There exists a medium risk of death. It is highly advisable to visit a doctor for a professional diagnosis.'
    elif prediction > 0.0:
        clfn = 'Low Risk'
        clfn_color = f':blue[{clfn}]'
        advice = 'Low risk of death. No specialized medical care is needed in this case.'
    return clfn, clfn_color, advice