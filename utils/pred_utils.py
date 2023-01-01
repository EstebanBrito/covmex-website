import json
from .req_utils import make_request
import random

def clean_input(input:dict) -> dict:
    for key, value in input.keys():
        if value == 'No': input[key] == 0
        if value == 'Sí': input[key] == 1
        if value == 'Hombre': input[key] == 0
        if value == 'Mujer': input[key] == 1
    return input

def predict_mort_pred(input:dict):
    print(input)
    return random.random()
    # Preprocess request
    cleaned_input = clean_input(input)
    input_json = json.dumps(cleaned_input)
    # Make request, get response
    response = make_request(input_json)
    # Preprocess response
    return response

def get_prediction_info(prediction):
    if prediction > 0.66:
        clfn = 'Riesgo Elevado'
        clfn_color = f':red[{clfn}]'
        advice = 'Atiéndase a la brevedad.'
    elif prediction > 0.33:
        clfn = 'Riesgo Medio'
        clfn_color = f':orange[{clfn}]'
        advice = 'Consulte a un médico para un diagnóstico más certero.'
    elif prediction > 0.0:
        clfn = 'Riesgo Bajo'
        clfn_color = f':blue[{clfn}]'
        advice = 'No son necesario cuidados mayores en este caso.'
    return clfn, clfn_color, advice