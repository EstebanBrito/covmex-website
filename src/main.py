import streamlit as st
from my_pages.home import render_home_page
from my_pages.mort_pred import render_mort_pred_page

st.set_page_config(
    page_title="Covid Mexico Platform",
    initial_sidebar_state='expanded'
)

pages = {
    'mort_pred': render_mort_pred_page,
    'home': render_home_page
}

def buttons():
    home = st.sidebar.button('Home', key='home-button')
    mort = st.sidebar.button('Mortality Prediction', key='mort-pred-button')
    if mort: return 'mort_pred'
    elif home: return 'home'
    else: return None


if __name__ == '__main__':
    # Global sidebar
    st.sidebar.markdown('# Lateral Menu #')
    st.sidebar.markdown('### Select a Page ###')
    selected_page = buttons()

    # Store current_page to remember it
    if selected_page is None:
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = 'home'
    else:
        st.session_state['current_page'] = selected_page

    # Render current page
    pages[st.session_state['current_page']]()