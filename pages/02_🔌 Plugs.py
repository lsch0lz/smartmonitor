import streamlit as st

if 'user_authentication' not in st.session_state:
    st.session_state['user_authentication'] = False

st.set_page_config(
    page_title="Smart-Plugs", 
    page_icon="🔌",
    )

if st.session_state['user_authentication'] == True:
    plugs = ['Meross MSS110', 'Meross MSS210', 'Meross MSS310']
    
    st.markdown("# Your Smart-Home Plugs:")
    st.sidebar.header("List of your Plugs:")
    for plug in plugs:
        st.sidebar.write(plug)