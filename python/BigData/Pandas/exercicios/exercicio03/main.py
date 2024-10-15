import pandas as pd
import json

# Carregar o arquivo JSON
with open("sample_data/clientes_compras.json", "r") as file:
    dados = json.load(file)

# Criar um DataFrame a partir dos dados JSON
df = pd.DataFrame(dados)

# Somar o valor das compras por cliente
soma_compras = df.groupby(['cliente_id', 'nome'])['valor_compra'].sum().reset_index()

# Filtrar apenas os clientes que compraram mais de uma vez
clientes_mais_de_uma_compra = df['cliente_id'].value_counts()
clientes_repetidos = clientes_mais_de_uma_compra[clientes_mais_de_uma_compra > 1].index

# Exibir o total de compras apenas dos clientes que compraram mais de uma vez
resultado = soma_compras[soma_compras['cliente_id'].isin(clientes_repetidos)]
# Ordenar pelo valor total de compras (em ordem decrescente)
resultado = resultado.sort_values(by='valor_compra', ascending=False)
print(f"Clientes que compraram mais de uma vez (com o valor total das compras): \n{resultado}")
