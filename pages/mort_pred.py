import streamlit as st
from utils.st_utils import markdown_h, dummy_text, sidebar
from utils.pred_utils import predict_mort_pred, get_prediction_info

# Inputs must be
# SEXO, EDAD, EMBARAZO, DIABETES,
# EPOC, ASMA, INMUSPR, HIPERTENSION,
# OTRA_COM, OBESIDAD, CARDIOVASCULAR, RENAL_CRONICA
# TABAQUISMO, DIAS_SINTOMAS

# Sidebar
sidebar()

# Actual page
st.title('Predicción de Mortalidad por COVID-19')
st.write('''
    Este servicio está destinado para predecir la probabilidad
    de muerte de una persona infectada por COVID-19, basándose
    en su información general y médica. \n
    Para usar el servicio, rellene el formulario debajo y
    presione el boton "Predecir" cuando esté listo. Podrá ver
    sus resultados y las explicaciones pertinentes de éste en
    la parte de abajo de la pagina.
''')
st.markdown('''
    **ADVERTENCIA: Las predicciones de este servicio no reemplazan
    el tratamiento y diagnóstico de médicos profesionales. Acuda
    a un médico para obtener una opinión más completa.**
''')
markdown_h('Información del Paciente', 3)

# Form
with st.form('Form') as form:
    col1, col2 = st.columns(2)
    # First column
    edad = col1.number_input('Edad', min_value=0, max_value=125, value=25, step=1, format='%d', help='', key='edad')
    embar = col1.radio('¿Está embarazada?', ('No', 'Sí'), key='embarazo')
    diab = col1.radio('¿Tiene diabetes?', ('No', 'Sí'), key='diabetes')
    epoc = col1.radio('¿Tiene EPOC (Enfermedad Pulmonar Obstructiva Crónica)?', ('No', 'Sí'), key='epoc')
    asma = col1.radio('¿Tiene asma?', ('No', 'Sí'), key='asma')
    inmu = col1.radio('¿Padece de inmunosupresión?', ('No', 'Sí'), key='inmusupr')
    dias_sint = col1.select_slider('¿Hace cuántos días presentó síntomas?', range(0, 15), value=3, key='dias-sintomas')
    # Second column
    sexo = col2.radio('Sexo', ('Hombre', 'Mujer'), key='sexo')
    hiper = col2.radio('¿Tiene hipertensión?', ('No', 'Sí'), key='hiper')
    obes = col2.radio('¿Sufre de obesidad?', ('No', 'Sí'), key='obesidad')
    cardio = col2.radio('¿Sufre de alguna enfermedad cardiovascular?', ('No', 'Sí'), key='cardio')
    renal = col2.radio('¿Tiene afecciones renales crónicas?', ('No', 'Sí'), key='renal')
    taba = col2.radio('¿Suele fumar con frecuencia?', ('No', 'Sí'), key='tabaquismo')
    otra = col2.radio('¿Sufre de alguna otra afección grave?', ('No', 'Sí'), key='otra-com')
    # Preparing input for remote model prediction
    pacient_info = {
        'EDAD': int(edad),
        'SEXO': sexo,
        'EMBARAZO': embar,
        'DIABETES': diab,
        'EPOC': epoc,
        'ASMA': asma,
        'INMUSUPR': inmu,
        'HIPERTENSION': hiper,
        'OTRA_COM': otra,
        'OBESIDAD': obes,
        'CARDIOVASCULAR': cardio,
        'RENAL_CRONICA': renal,
        'TABAQUISMO': taba,
        'DIAS_SINTOMAS': int(dias_sint)
    }
    # Form submission button
    st.form_submit_button('Predecir')

# Making prediction
prediction = predict_mort_pred(pacient_info, mocked=False)
_, risk_clfn, risk_advice = get_prediction_info(prediction)

# Prediction Results
markdown_h('Resultados', 1)
c1, c2 = st.columns((1, 2))
## Prediction Percentage
markdown_h('Probabilidad de Muerte', 3, ctx=c1)
prediction_pct = round(prediction*100, 2)
c1.metric(value=f'{prediction_pct} %', label='_', label_visibility='hidden')
c1.progress(prediction)
## More information about prediction
markdown_h('Clasificación', 3, ctx=c2)
c2.markdown(f'##### {risk_clfn} #####')
markdown_h('Indicaciones', 3, ctx=c2)
c2.write(risk_advice)
## Explaining the Results
markdown_h('¿Que significan estos resultados?', 4)
exp = st.expander('Presiona para conocer más', expanded=False)
exp.write('''
    La probabilidad de muerte es calculada con una técnica de
    Inteligencia Artificial llamada Bosque Aleatorio,
    y determina el porcentaje de personas
    parecidas al paciente en cuestión que fallecieron debido a
    COVID-19 en los últimos tres meses. \n
    Este porcentaje determina el nivel de riesgo en el que se
    encuentra el paciente y las indicaciones recomendadas:
    * Riesgo Bajo: Menos de 1 de cada 3 personas similares al paciente fallecieron debido a COVID-19. Si el paciente guarda reposo y cuidados adecuados, no debería complicarse su situación médica.
    * Riesgo Medio: Alrededor de la mitad de las personas similares al paciente fallecieron, y es necesario un diagnóstico médico para determinar si el paciente se encuentra en riesgo o no, y emitir indicaciones adecuadas.
    * Riesgo Alto: Al menos 2 de cada 3 personas similares al paciente fallecieron debido a COVID-19. Es muy probable que la situación médica de la persona empeore y debería ser atendida por un médico a la brevedad.
''')
exp.markdown('Puedes conocer a mayor profundidad cómo funciona nuestra tecnología [aquí]()')