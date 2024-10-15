import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o conjunto de dados a partir de um arquivo CSV
dados = pd.read_csv("sample_data/dados.csv")

# Converter a coluna 'data' para o formato de data
dados['data'] = pd.to_datetime(dados['data'])

# Calcular o valor total de vendas por região
vendas_por_regiao = dados.groupby('regiao')['valor'].sum().reset_index()

# Exibir o valor total de vendas por região
print(vendas_por_regiao)

# Calcular o valor total de vendas por região e data para o gráfico
vendas_por_regiao_data = dados.groupby(['data', 'regiao'])['valor'].sum().reset_index()

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar o gráfico de barras empilhadas por região e data
plt.figure(figsize=(10, 6))
sns.barplot(x="data", y="valor", hue="regiao", data=vendas_por_regiao_data, palette="viridis")

# Ajustar rótulos e título
plt.xlabel('Data')
plt.ylabel('Valor de Vendas')
plt.title('Vendas por Região e Data')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
