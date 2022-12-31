import streamlit as st
from utils.st_utils import markdown_h, sidebar, dummy_text, person

if __name__ == '__main__':
    sidebar()

    st.title('Plataforma Mexico Covid')
    markdown_h('¿Qué Somos?', 2)
    dummy_text()
    markdown_h('¿Qué Hacemos?', 2)
    dummy_text(2)
    markdown_h('¿Cómo lo hacemos?', 2)
    dummy_text()
    markdown_h('Conoce al equipo', 2)
    cols = st.columns(4)
    person(cols[0], 'Esteban Brito', 'Científico de Datos')
    person(cols[1], 'Daniel Cruz', 'Ingeniero de Datos')
    person(cols[2], 'Héctor Ruiz', 'Analista de Datos')
    person(cols[3], 'Esperanza Ek', 'Analista de Datos')


