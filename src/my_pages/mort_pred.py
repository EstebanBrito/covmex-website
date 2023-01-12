import streamlit as st
from utils.st_utils import markdown_h, dummy_text
from utils.pred_utils import predict_mort_pred, get_prediction_info

def format_sex(sex):
    if sex == 'Hombre': return 'Man'
    elif sex == 'Mujer': return 'Woman'

def format_yes_no(opt):
    if opt == 'Sí': return 'Yes'
    elif opt == 'No': return 'No'

# Inputs must be
# SEXO, EDAD, EMBARAZO, DIABETES,
# EPOC, ASMA, INMUSPR, HIPERTENSION,
# OTRA_COM, OBESIDAD, CARDIOVASCULAR, RENAL_CRONICA
# TABAQUISMO, DIAS_SINTOMAS
def render_mort_pred_page():
    # Actual page
    st.title('COVID-19 Mortality Prediction')
    st.write('''
        This service predicts the probability of death of a COVID-19
        infected person, taking into consideration medical and general
        information. \n
        It order to use the service, fill up the form below, and click
        the "Predict" button when you're ready. Your results will be
        shown at the bottom of the webpage. Be sure to read the 
        explanations about what they represent, too! \n
    ''')
    st.markdown('''
        **DISCLAIMER: The predictions of this service DO NOT
        substitute the diagnose of a certified health professional.
        Our goal is to give a quick assessment of a patient's situation,
        not to provide medical treatment. Go to the hospital if you
        ever need to.**
    ''')
    markdown_h('Pacient\'s information', 3)

    # Form
    with st.form('Form') as form:
        # Form will have two columns
        col1, col2 = st.columns(2)
        # First column
        edad = col1.number_input('Age', min_value=0, max_value=125, value=25, step=1, format='%d', help='', key='edad')
        sexo = col1.radio('Sex', ('Hombre', 'Mujer'), format_func=format_sex, key='sexo')
        embar = col1.radio('Are you pregnant?', ('No', 'Sí'), format_func=format_yes_no, key='embarazo')
        diab = col1.radio('Do you have diabetes?', ('No', 'Sí'), format_func=format_yes_no, key='diabetes')
        epoc = col1.radio('¿Do you have COPD (Chronic Obstructive Pulmonary Disease)?', ('No', 'Sí'), format_func=format_yes_no, key='epoc')
        asma = col1.radio('Do you have asthma?', ('No', 'Sí'), format_func=format_yes_no, key='asma')
        inmu = col1.radio('Do you suffer from immunosupression?', ('No', 'Sí'), format_func=format_yes_no, key='inmusupr')
        # Second column
        hiper = col2.radio('Do you have hypertension?', ('No', 'Sí'), format_func=format_yes_no, key='hiper')
        obes = col2.radio('Do you suffer from obesity?', ('No', 'Sí'), format_func=format_yes_no, key='obesidad')
        cardio = col2.radio('Do you have any other cardiovascular afffections?', ('No', 'Sí'), format_func=format_yes_no, key='cardio')
        renal = col2.radio('Do you suffer from chronic renal failure?', ('No', 'Sí'), format_func=format_yes_no, key='renal')
        taba = col2.radio('Do you frequently smoke?', ('No', 'Sí'), format_func=format_yes_no, key='tabaquismo')
        otra = col2.radio('Do you have any other relevant additional affections?', ('No', 'Sí'), format_func=format_yes_no, key='otra-com')
        dias_sint = col2.select_slider('How many days ago did the first symptoms appear?', range(0, 15), value=3, key='dias-sintomas')
        # Form submission button
        st.form_submit_button('Predict')

    # Making prediction
    ## Preparing input for remote model prediction
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
    prediction = predict_mort_pred(pacient_info, mocked=False)
    _, risk_clfn, risk_advice = get_prediction_info(prediction)

    # Prediction Results
    markdown_h('Results', 1)
    c1, c2 = st.columns((1, 2))
    ## Prediction Percentage
    markdown_h('Probability of Death', 3, ctx=c1)
    prediction_pct = round(prediction*100, 2)
    c1.metric(value=f'{prediction_pct} %', label='_', label_visibility='hidden')
    c1.progress(prediction)
    ## More information about prediction
    markdown_h('Classification', 3, ctx=c2)
    markdown_h(risk_clfn, 5, ctx=c2)
    markdown_h('Indications', 3, ctx=c2)
    c2.write(risk_advice)
    ## Explaining the Results
    markdown_h('What do these results represent?', 4)
    exp = st.expander('Click to know more...', expanded=False)
    exp.write('''
        The probability of death is calculated using an Artificial
        Intelligence model called Random Forest, which,
        given the information of a person, determines
        the percentage of similar cases of people that died due
        to COVID-19 in the last three months. \n
        This percentage determines both the risk the patient faces
        and the general indications he/she should follow:
        * Low Risk: Less than 1 of every 3 similar patients died due to COVID-19. If the patient keeps rest and proper care, his medical situation should not aggravate.
        * Medium Risk: About half of the similar patients died due to COVID-19, and a professional medical diagnosis is necessary to determine whether the patient is at risk and to issue appropriate indications.
        * High Risk: At least 2 out of 3 similar patients died due to COVID-19. The person's medical situation is likely to worsen and should be treated by a doctor as soon as possible.
    ''')
    # exp.markdown('Puedes conocer a mayor profundidad cómo funciona nuestros servicios en la sección "Nuestra tecnología", presente en el menú lateral')