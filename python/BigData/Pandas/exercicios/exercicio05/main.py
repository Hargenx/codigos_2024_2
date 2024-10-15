import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados a partir do arquivo Excel
df = pd.read_excel("sample_data/clientes_compras.xlsx", sheet_name="Compras")

# Converter a coluna 'data_compra' para o formato datetime
df['data_compra'] = pd.to_datetime(df['data_compra'])

# Exibir os primeiros dados para verificar
print(df.head())

# Gráfico de Dispersão (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='data_compra', y='valor_compra', hue='nome', data=df, palette='viridis', s=100)

# Ajustar rótulos e título
plt.xlabel('Data da Compra')
plt.ylabel('Valor da Compra')
plt.title('Dispersão do Valor das Compras por Cliente ao Longo do Tempo')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()

# Gráfico de Linha (Evolução das Compras ao Longo do Tempo)
plt.figure(figsize=(10, 6))
sns.lineplot(x='data_compra', y='valor_compra', hue='nome', data=df, marker='o', palette='viridis')

# Ajustar rótulos e título
plt.xlabel('Data da Compra')
plt.ylabel('Valor da Compra')
plt.title('Evolução das Compras ao Longo do Tempo por Cliente')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
