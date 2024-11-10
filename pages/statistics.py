import streamlit as st
import utility as utility
import logica as daia
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import matplotlib.pyplot as plt



import pandas as pd


st.title('Estadisticas')


def obtener_datos_cvs():
    db, _ = daia.init_firebase()  # Usamos tu función para inicializar Firebase

    # Obtener todos los documentos de la colección 'cvs'
    docs = db.collection('cvs').stream()

    # Almacenar datos en una lista para luego convertir en DataFrame
    data_list = []
    for doc in docs:
        data = doc.to_dict()
        data_list.append(data)

    # Convertir la lista de diccionarios en un DataFrame de pandas
    df = pd.DataFrame(data_list)
    return df

def analizar_datos(df):
    # Análisis de cantidad de tipos de archivos subidos
    df['file_type'] = df['cv_filename'].apply(lambda x: x.split('.')[-1])
    
    # Contar cuántos archivos de cada tipo hay
    file_type_counts = df['file_type'].value_counts()
    
    return file_type_counts

import streamlit as st
import matplotlib.pyplot as plt

def mostrar_graficos(file_type_counts):
    # Mostrar gráfico de barras con los tipos de archivos subidos
    st.bar_chart(file_type_counts)

    # Usar matplotlib para crear un gráfico circular (pie chart)
    fig, ax = plt.subplots()
    ax.pie(file_type_counts, labels=file_type_counts.index, autopct='%1.1f%%')
    ax.set_title("Distribución de tipos de archivo subido")
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

utility.generar_menu()


df = obtener_datos_cvs()
 # Analizar los datos
file_type_counts = analizar_datos(df)

    # Mostrar gráficos
mostrar_graficos(file_type_counts)


daia.get_data_and_analyze()

