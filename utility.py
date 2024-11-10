import streamlit as st

def generar_menu():
    with st.sidebar:
      st.page_link('main.py', label= "Inicio", icon="🏠")  
      
      st.page_link('pages/statistics.py', label= "Estadisticas", icon="📈")
      st.page_link('pages/config.py', label= "Configuracion", icon="⚙️")
      st.page_link('pages/login.py', label= "Ingresar", icon="🔓")
