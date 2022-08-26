import streamlit as st
from streamlit_option_menu import option_menu

from src.utils.login import check_login

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
)

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to your Smart-Monitor</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Here you can monitor ALL of your Smart-Home-Devices</h2>", unsafe_allow_html=True)

username = st.text_input('Username', '')
password = st.text_input('Password',  '')

if st.button('Login'):
        if check_login(username, password):
            st.write("Sucessfully Loged in!")
        else:
            st.write("Wrong PW")
        
st.write('No Account yet? Create one!')
if st.button('Register'):
        pass