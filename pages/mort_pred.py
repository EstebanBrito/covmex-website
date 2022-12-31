import streamlit as st
from utils.st_utils import markdown_h, dummy_text, sidebar
from utils.req_utils import predict_mort_pred

# Inputs must be
# SEXO, EDAD, EMBARAZO, DIABETES,
# EPOC, ASMA, INMUSPR, HIPERTENSION,
# OTRAS_COM, OBESIDAD, RENAL_CRONICA, TABAQUISMO,
# DIAS_SINTOMAS

# Sidebar
sidebar()

# Actual page
st.title('Predicción de Mortalidad por COVID')
dummy_text()
markdown_h('Información del Paciente', 3)
with st.form('Form') as form:
    col1, col2 = st.columns(2)
    # First column
    edad = col1.number_input('Edad', min_value=0, max_value=125, value=20, step=1, format='%d', help='', key='edad')
    embar = col1.radio('¿Está embarazada?', ('No', 'Sí'), key='embarazo')
    diab = col1.radio('¿Tiene Diabetes?', ('No', 'Sí'), key='diabetes')
    epoc = col1.radio('¿Tiene EPOC?', ('No', 'Sí'), key='epoc')
    asma = col1.radio('¿Tiene Asma?', ('No', 'Sí'), key='asma')
    inmu = col1.radio('¿Tiene Inmunosupresión?', ('No', 'Sí'), key='inmusupr')
    dias_sint = col1.select_slider('¿Hace cuántos días presentó síntomas?', range(0, 15), value=3, key='dias-sintomas')
    # Second column
    sexo = col2.radio('Sexo', ('Hombre', 'Mujer'), key='sexo')
    hiper = col2.radio('¿Tiene Hipertensión?', ('No', 'Sí'), key='hiper')
    obes = col2.radio('¿Sufre de Obesidad?', ('No', 'Sí'), key='obesidad')
    renal = col2.radio('¿Tiene afecciones renales?', ('No', 'Sí'), key='renal')
    taba = col2.radio('¿Sufre de Tabaquismo?', ('No', 'Sí'), key='tabaquismo')
    otra = col2.radio('¿Sufre de alguna otra afección grave?', ('No', 'Sí'), key='otra-com')
    
    # Preparing input for remote model prediction
    input = {
        'EDAD': int(edad),
        'EMBAZARO': embar,
        'DIABETES': diab,
        'EPOC': epoc,
        'ASMA': asma,
        'INMUSUPR': inmu,
        'HIPERTENSION': hiper,
        'OTRAS_COM': otra,
        'OBESIDAD': obes,
        'RENAL_CRONICA': renal,
        'TABAQUISMO': taba,
        'DIAS_SINTOMAS': int(dias_sint)
    }
    # prediction = predict_mort_pred(input)
    # 
    st.form_submit_button('Predecir')
