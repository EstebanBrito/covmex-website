import streamlit as st
from utils.st_utils import markdown_h, dummy_text, person

def render_home_page():
    st.title('Covix Mexico Platform (CovMex)')
    markdown_h('What we are?', 2)
    st.write('''
        CovMex is a web-based platform designed to supply helpful
        information and services to the general mexican public in order
        to help them better understand and cope with the current COVID-19 pandemic.
    ''')
    # dummy_text()
    markdown_h('What do we do?', 2)
    st.write('''
        Our team of engineers develops software tools and services that are
        useful and easy to use for the average citizen. One of our services, for
        example, is designed to help users understand the risk of getting infected
        of COVID by calculating their probabilities of death when compared to
        previous similar cases of SARS-CoV-2 (check it out by opening the lateral
        menu!). \n
        Our roadmap of future features include:
        * A life expectancy forecasting service, to calculate the approximate time of life critical pacients have before dying, helping medical personnel to better focus their effort and talent.
        * A recovery time forecasting service, that estimates the average time a non-critical hospitalized pacient is going to spend at the hospital to recover, providing a way to predict hospital occupation rates in advance.
        * General interactive visualization tools so every mexican citizen has access to updated information about infections, deaths and recent upbursts of COVID-19 cases all acrooss the country. 
    ''')
    # dummy_text(2)
    markdown_h('How do we do it?', 2)
    st.write('''
        Our core services are built leveraging the power of Artificial
        Intelligence and Data Science to provide realiable and accurate
        tools to fulfull our mission. Our whole approach to tackle obstacles
        and challenged is based on software and technology, automating tasks
        and processes in order to save resources and use them where
        they are really needed.
    ''')
    # dummy_text()
    markdown_h('Meet the Team', 2)
    st.write('''
        All of this is possible thanks to a handful of people that
        dedicate part of their time towards building our platform!
    ''')
    cols = st.columns(4)
    # paths are relative to projects' root folder
    person('Esteban Brito', 'Data Scientist', photo_path='src/assets/esteban.jpg', ctx=cols[0])
    person('Daniel Cruz', 'Data Engineer', photo_path='src/assets/daniel.jpg', ctx=cols[1])
    person('Héctor Ruiz', 'Data Analyst', photo_path='src/assets/hector.jpg', ctx=cols[2])
    person('Esperanza Ek', 'Data Analyst', photo_path='src/assets/esperanza.jpg', ctx=cols[3])


