# streamlit_app.py
import streamlit as st
import pandas as pd
import requests
from app.data_loader import DataLoader
from app.analysis import Analysis

# Carregar e pré-processar os dados
data_loader = DataLoader('titanic.csv')
data = data_loader.load_data()
data_loader.preprocess_data()
analysis = Analysis(data)

# Título
st.title("Análise do Titanic com Flask e Streamlit")

# Visualizar dados
st.header("Dados do Titanic")
st.write(data.head())

# Taxa de sobrevivência
st.header("Taxa de Sobrevivência")
rate = requests.get("http://127.0.0.1:5000/api/survival_rate").json()["survival_rate"]
st.write(f"Taxa de sobrevivência: {rate:.2%}")

# Filtro por passageiro
st.header("Informações do Passageiro")
passenger_id = st.number_input("ID do Passageiro", min_value=1, max_value=int(data['PassengerId'].max()), value=1)
passenger_data = requests.get(f"http://127.0.0.1:5000/api/passenger/{passenger_id}").json()
st.write(passenger_data)

# Distribuição de idade
st.header("Distribuição de Idade dos Passageiros")
fig = analysis.plot_age_distribution()
st.pyplot(fig)
