import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Analisis de datos de vehiculos en estados unidos')

# Botones para histogramas y gráficos de dispersión
if st.checkbox('Mostrar histograma'):
    columna = st.selectbox('Selecciona una columna para el histograma', df.columns)
    fig = px.histogram(df, x=columna)
    st.plotly_chart(fig)

if st.checkbox('Mostrar gráfico de dispersión'):
    columna_x = st.selectbox('Selecciona la columna X', df.columns)
    columna_y = st.selectbox('Selecciona la columna Y', df.columns)
    fig = px.scatter(df, x=columna_x, y=columna_y)
    st.plotly_chart(fig)