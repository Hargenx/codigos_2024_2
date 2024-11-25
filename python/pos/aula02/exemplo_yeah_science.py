import pandas as pd
import matplotlib.pyplot as plt

# Criação de um DataFrame
dados = {'Ano': [2018, 2019, 2020, 2021, 2022, 2023, 2024], 'Vendas': [120, 152, 188, 200, 215, 212, 208]}
df = pd.DataFrame(dados)

# Plotando os dados
plt.plot(df['Ano'], df['Vendas'])
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.title('Vendas por Ano')
plt.show()
