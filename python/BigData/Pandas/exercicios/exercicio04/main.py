import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo JSON
with open("sample_data/clientes_compras.json", "r") as file:
    dados = json.load(file)

# Criar um DataFrame a partir dos dados JSON
df = pd.DataFrame(dados)

# Converter a coluna de data para o formato datetime
df['data_compra'] = pd.to_datetime(df['data_compra'])

# Criar um gráfico de dispersão (scatter plot)
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
