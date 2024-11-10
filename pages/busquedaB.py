import streamlit as st
import utility as utility
from databaseConnection import save_form_data


utility.generar_menu()

st.title('Aplicar al puesto Frontend')

formB = st.form(key='formB')
firstname = formB.text_input("Nombre")
lastname = formB.text_input("Apellido")
city = formB.text_input("Ciudad")
address = formB.text_input("Direccion")
mail = formB.text_input("Email")

cv =formB.file_uploader("Sube tu CV (PDF)", type=['jpg','png','pdf'])

submit_button = formB.form_submit_button("Aplicar")

if submit_button:
    if not firstname or not lastname or not mail or not cv:
        st.error("Por favor, completa todos los campos.")
    else:
        cv_id,cv_url = save_form_data(firstname, lastname, address, mail, cv)
        st.success(f"Gracias {firstname}, tu CV ha sido enviado correctamente.ID generado: {cv_id}")