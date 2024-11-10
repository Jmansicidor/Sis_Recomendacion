import streamlit as st
import utility as utility

utility.generar_menu()

st.title('🤖 Sistema para la seleccion de personal')





st.write("""
        En la empresa X estamos buscando un programador backend jr con las siguinetes habilidades: 

         * Java
         * Ingles
         * Base de Datos"""
         )
btnOfertaA = st.button('Aplicar a la Oferta A')

st.write("""
           En la empresa X estamos buscando un programador frontend jr con las siguinetes habilidades: 

         * JavaScrpit
         * Angular
         * CSS, HTML"""
         )
btnOfertaB = st.button('Aplicar a la Oferta B')


if btnOfertaA:
    st.switch_page('pages/busquedaA.py')

if btnOfertaB:
    st.switch_page('pages/busquedaB.py')

