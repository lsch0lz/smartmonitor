import streamlit as st

from src.utils.login import check_login
from src.utils.register import create_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
)

if 'user_authentication' not in st.session_state:
    st.session_state['user_authentication'] = False

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to your Smart-Monitor</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Here you can monitor ALL of your Smart-Home-Devices</h2>", unsafe_allow_html=True)

username = st.text_input('Username', '')
password = st.text_input('Password',  '')

if st.button('Login'):
        if check_login(username, password):
            st.write('Welcome to Smart-Monitor!')
            st.session_state['user_authentication'] = True
        else:
            st.write("Wrong Credetentials! Try Again!")
            st.session_state['user_authentication'] = False
        
st.write('No Account yet? Create one! Just fill out the fields with your new Username and Password.')
if st.button('Register'):
        if create_user(username, password):
            st.write('Welcome to Smart-Monitor!')
            st.session_state['user_authentication'] = True