import streamlit as st

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'

def sidebar() -> None:
    st.sidebar.header('Nuestros Servicios')
    st.sidebar.button('Servicio 1', key='1')
    st.sidebar.button('Servicio 2', key='2')
    st.sidebar.button('Servicio 3', key='3')
    st.sidebar.image('assets/logo.jpg', width=50)

def markdown_h(text:str, level:int=1) -> None:
    h_markers = '#' * level
    markdown_text = f'{h_markers} {text} {h_markers}'
    st.markdown(markdown_text)

def dummy_text(paragraphs=1):
    final_text = ''
    for i in range(paragraphs):
        final_text += lorem_ipsum
        final_text += '\n'
    st.write(final_text)

def person(widget, name, role, photo_path='assets/logo.jpg'):
    widget.image(photo_path, width=50)
    widget.markdown(f'**{name}**') # Bold
    widget.markdown(f'_{role}_') # Italic
