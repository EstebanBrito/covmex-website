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

def predict_mort_pred(input:dict, mocked:bool=True):
    # Preprocess input
    cleaned_input = clean_input(input)
    input_json = json.dumps(cleaned_input)
    # Make request, get response
    if mocked: response_json = [ [ random.random() ] ]
    else: response_json = make_request(input_json)
    # Preprocess response
    prediction = response_json # json.loads(response_json) # response_json is already a list: no need to parse it from JSON
    prediction = prediction[0][0] # [instances][prediction_outputs]
    return prediction

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