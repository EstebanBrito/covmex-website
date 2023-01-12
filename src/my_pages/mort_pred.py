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
        ever need to. Also, this service was created taking into 
        consideration only confirmed cases of COVID-19, so it does not work
        to assess other affections.**
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
        This service was built using an Artificial Intelligence (AI)
        model called Random Forest, which, given the information
        of a person, determines if he/she is going to die due to
        COVID-19, and also returns a "confidence score" that specifies
        the confidence of the prediction. \n
        A Random Forest uses under the hood a high number of "dumb"
        auxiliary models, called Decision Trees, that are trained to estimate the probability
        of death of people belonging to different sectors of the population.
        The confidence score is computed by averaging the probabilities of all the trees,
        but a 40\% confidence ratio, for example, should not be interpreted as "4 out
        of every 10 similar patients died due to COVID-19", because each
        tree only analyzes a specific sector of the patient population,
        not all individuals, and thus, the probability of an individual
        tree is likely to be wrong. \n
        However, when probabilities are aggregated, we obtain a score that,
        when it's higher than 50%, can accurately detect patients in
        risk of death. This behavior is analogous to the concept of "wisdom
        of the crowd", where the opinion of a single "tree" is likely
        to be wrong or incomplete, but the opinion of the whole "forest" can
        be accurate and reliable. \n
        The confidence score is also used to determine the patient's
        risk level and the general indications he/she should follow: \n
        * Low Risk: A score lower than 40\% means that the patient IS NOT likely to die due to COVID-19, and if the patient keeps rest and proper care, his/her medical situation should not aggravate..
        * Medium Risk: AI models are not perfect, and a confidence score around 50\% means the prediction could be either right or wrong, and additional information is required, such as the opinion of a professional medic.
        * High Risk: High Risk: A score higher than 60% means the patient IS likely to die due to COVID-19 and he/she should be treated by medical professionals as soon as possible.
    ''')
    # exp.markdown('Puedes conocer a mayor profundidad cómo funciona nuestros servicios en la sección "Nuestra tecnología", presente en el menú lateral')