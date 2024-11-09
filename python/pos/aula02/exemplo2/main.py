import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
data = pd.read_csv('Imports_Exports_Dataset new.csv')

# Traduzir os nomes das colunas para português
data.rename(columns={
    'Transaction_ID': 'ID_Transação',
    'Country': 'País',
    'Product': 'Produto',
    'Import_Export': 'Tipo',
    'Shipping_Method': 'Método_Envio',
    'Port': 'Porto',
    'Category': 'Categoria',
    'Quantity': 'Quantidade',
    'Value': 'Valor',
    'Date': 'Data',
    'Customs_Code': 'Código_Aduaneiro',
    'Weight': 'Peso'
}, inplace=True)

# Configuração do app Streamlit
st.title("Visualização de Dados de Importações e Exportações")

# Barra lateral para opções de filtragem
st.sidebar.header("Opções de Filtro")

# Filtro por País (com busca)
pais_selecionado = st.sidebar.selectbox(
    "Selecione o País", 
    options=data["País"].unique(),
    index=0
)

# Filtro por Importação ou Exportação
tipo_selecionado = st.sidebar.radio(
    "Importação ou Exportação", 
    options=data["Tipo"].unique()
)

# Filtro por Categoria
categorias_selecionadas = st.sidebar.multiselect(
    "Selecione Categorias",
    options=data["Categoria"].unique(),
    default=data["Categoria"].unique()
)

# Aplicar filtros ao dataset
dados_filtrados = data[(data["País"] == pais_selecionado) & 
                       (data["Tipo"] == tipo_selecionado) & 
                       (data["Categoria"].isin(categorias_selecionadas))]

# Exibir dados filtrados
st.write(f"### Dados Filtrados para {pais_selecionado}", dados_filtrados)

# Visualização 1: Quantidade por País
quantidade_por_categoria = dados_filtrados.groupby("Categoria")["Quantidade"].sum().reset_index()
fig_quantidade = px.bar(quantidade_por_categoria, x="Categoria", y="Quantidade", 
                        title=f"Quantidade Total por Categoria - {pais_selecionado}")
st.plotly_chart(fig_quantidade)

# Visualização 2: Valor por Categoria
valor_por_categoria = dados_filtrados.groupby("Categoria")["Valor"].sum().reset_index()
fig_valor = px.pie(valor_por_categoria, names="Categoria", values="Valor", 
                   title=f"Valor Total por Categoria - {pais_selecionado}")
st.plotly_chart(fig_valor)

# Visualização 3: Peso ao longo do tempo
dados_filtrados['Data'] = pd.to_datetime(dados_filtrados['Data'], format='%d-%m-%Y')
peso_ao_longo_tempo = dados_filtrados.groupby("Data")["Peso"].sum().reset_index()
fig_peso = px.line(peso_ao_longo_tempo, x="Data", y="Peso", 
                   title=f"Peso Total ao Longo do Tempo - {pais_selecionado}")
st.plotly_chart(fig_peso)

# Rodapé
st.write("Esta aplicação utiliza Pandas, Plotly e Streamlit para visualização de dados.")
