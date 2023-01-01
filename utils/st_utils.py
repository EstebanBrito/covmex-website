import streamlit as st

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'

def sidebar() -> None:
    st.sidebar.header('Nuestros Servicios')
    st.sidebar.button('Servicio 1', key='1')
    st.sidebar.button('Servicio 2', key='2')
    st.sidebar.button('Servicio 3', key='3')
    st.sidebar.image('assets/logo.jpg', width=50)

def markdown_h(text:str, level:int=1, ctx=st) -> None:
    h_markers = '#' * level
    markdown_text = f'{h_markers} {text} {h_markers}'
    ctx.markdown(markdown_text)

def dummy_text(paragraphs=1, ctx=st):
    final_text = ''
    for _ in range(paragraphs):
        final_text += lorem_ipsum + '\n'
    ctx.write(final_text)

def person(name, role, photo_path='assets/logo.jpg', ctx=st):
    ctx.image(photo_path, width=50)
    ctx.markdown(f'**{name}**') # Bold
    ctx.markdown(f'_{role}_') # Italic
