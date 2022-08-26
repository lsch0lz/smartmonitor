import streamlit as st

if 'user_authentication' not in st.session_state:
    st.session_state['user_authentication'] = False

st.set_page_config(
    page_title="Home-Dashboard", 
    page_icon="🏡",
    )

if st.session_state['user_authentication'] == True:
    st.write('Hello World!')
