import json
from .req_utils import make_request
import random
from time import sleep

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

def predict_mort_pred(input:dict):
    # Preprocess input
    cleaned_input = clean_input(input)
    input_json = json.dumps(cleaned_input)
    sleep(1)
    return random.random()
    # Make request, get response
    response = make_request(input_json)
    # Preprocess response
    return response

def get_prediction_info(prediction):
    if prediction > 0.66:
        clfn = 'Riesgo Elevado'
        clfn_color = f':red[{clfn}]'
        advice = 'Riesgo elevado de muerte. Atiéndase a la brevedad.'
    elif prediction > 0.33:
        clfn = 'Riesgo Medio'
        clfn_color = f':orange[{clfn}]'
        advice = 'Posible riesgo de muerte. Consulte a un médico para un diagnóstico más certero.'
    elif prediction > 0.0:
        clfn = 'Riesgo Bajo'
        clfn_color = f':blue[{clfn}]'
        advice = 'Riesgo bajo de muerte. No son necesarios cuidados mayores en este caso.'
    return clfn, clfn_color, advice