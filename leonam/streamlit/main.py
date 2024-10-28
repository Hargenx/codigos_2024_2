import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(layout="wide")
st.title("Bem-vinda, Anna Mendes")
st.write("Esse é seu relatório de Avaliação Física, Fisioterapia e Análise de Desempenho")

# Columns for general information
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avaliação", "1ª Avaliação", "16/10/2024")
col2.metric("Idade", "17 anos", "29/06/1994")
col3.metric("Peso", "58,8kg", "+0%")
col4.metric("Altura", "1,63cm", "+0%")

# Historical chart (mock data)
data = {
    "Mês": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Resultado": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325]
}

df = pd.DataFrame(data)

# Plot
st.write("### Histórico")
fig, ax = plt.subplots()
ax.plot(df["Mês"], df["Resultado"], marker='o')
ax.set_xlabel("Mês")
ax.set_ylabel("Resultado")
st.pyplot(fig)

# Columns for current results
st.write("### Resultados Atuais")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Peso Magro", "15%", "+18%")
col2.metric("Peso Gordo", "15%", "+18%")
col3.metric("% Gordura", "15%", "+18%")
col4.metric("IMC", "15%", "+18%")

# Footer logo (mock representation with text)
st.write("###")
st.write("Next Step - Fisical Performance")

