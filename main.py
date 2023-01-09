import streamlit as st
from my_pages.home import render_home_page
from my_pages.mort_pred import render_mort_pred_page

pages = {
    'mort_pred': render_mort_pred_page,
    'home': render_home_page
}

def buttons():
    home = st.sidebar.button('Inicio', key='home-button')
    mort = st.sidebar.button('Predicción de Mortalidad', key='mort-pred-button')
    if mort: return 'mort_pred'
    elif home: return 'home'
    else: return None


if __name__ == '__main__':
    # Metadata
    st.set_page_config(
        page_title="Plataforma Covid Mexico",
    )

    # Global sidebar
    st.sidebar.header('Nuestras páginas')
    selected_page = buttons()
    st.sidebar.image('assets/logo.jpg', width=50)

    # Store current_page to remember it
    if selected_page is None:
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = 'home'
    else:
        st.session_state['current_page'] = selected_page

    # Render current page
    pages[st.session_state['current_page']]()