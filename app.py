import streamlit as st
from utils.st_utils import markdown_h, sidebar, dummy_text, person

if __name__ == '__main__':
    sidebar()

    st.title('Plataforma Covid Mexico (CovMex)')
    markdown_h('¿Qué Somos?', 2)
    st.write('''
        CovMex es una plataforma web destinada a ofrecer herramientas
        informáticas a la ciudadanía mexicana con el objetivo de
        auxiliarles en sobrellevar la actual pandemia de SARS-COV-2.
    ''')
    # dummy_text()
    markdown_h('¿Qué Hacemos?', 2)
    st.write('''
        Desarrollamos herramientas informáticas que ayuden al 
        ciudadano mexicano promedio a sobrellevar la pandemia.
    ''')
    # dummy_text(2)
    markdown_h('¿Cómo lo hacemos?', 2)
    st.write('''
        Hacemos uso de tecnologías basadas en Inteligencia Artificial
        y Ciencia de Datos para contruir los servicios que proveemos.
    ''')
    # dummy_text()
    markdown_h('Conoce al equipo', 2)
    cols = st.columns(4)
    person('Esteban Brito', 'Científico de Datos', ctx=cols[0])
    person('Daniel Cruz', 'Ingeniero de Datos', ctx=cols[1])
    person('Héctor Ruiz', 'Analista de Datos', ctx=cols[2])
    person('Esperanza Ek', 'Analista de Datos', ctx=cols[3])


