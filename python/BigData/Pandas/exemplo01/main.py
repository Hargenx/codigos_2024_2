'''import json
# Carregar o arquivo JSON com os dados de bônus
with open('sample_data/bonus.json', 'r') as file:
    dados_bonus = json.load(file)'''

import pandas as pd

dados = pd.read_json('dados.json', typ='series')

# Criar DataFrame a partir do dicionário
df = pd.DataFrame(list(dados.items()), columns=['Nome', 'Salário'])

# Adicionando uma nova coluna "Bônus" (exemplo com 10% do salário)
df['Bônus'] = df['Salário'] * 0.10

# Como não existe a coluna "Cargo", vamos criar uma para fazer as próximas operações
# Vamos adicionar valores de cargo de exemplo
df['Cargo'] = ['Gerente', 'Assistente', 'Diretor', 'Analista', 'Estagiário', 'Estagiário', 'Analista', 'Diretor', 'Gerente', 'Diretor']

# Renomear a coluna "Cargo" para "Título do Cargo"
df.rename(columns={'Cargo': 'Título do Cargo'}, inplace=True)

# Agregar dados: calcular a média dos salários por título do cargo
agregado = df.groupby('Título do Cargo')['Salário'].mean().reset_index()
agregado.rename(columns={'Salário': 'Média de Salário'}, inplace=True)

# Ordenar o DataFrame pelo nome em ordem decrescente
df.sort_values(by='Nome', ascending=False, inplace=True)

# Exibir o DataFrame resultante com as operações
print(f"DataFrame com operações realizadas:\n{df}\n")

# Organizar o DataFrame 'agregado' pela média de salário em ordem decrescente
agregado_ordenado = agregado.sort_values(by='Média de Salário', ascending=False)

# Exibir o DataFrame 'agregado' organizado pela média de salário
print(f"\nMédia de Salário por Título do Cargo:\n{agregado_ordenado}\n")

import matplotlib.pyplot as plt

# Calcular a média dos salários por título do cargo
agregado = df.groupby('Título do Cargo')['Salário'].mean().reset_index()
agregado.rename(columns={'Salário': 'Média de Salário'}, inplace=True)

# Gráfico 1: Salário por Funcionário
plt.figure(figsize=(10, 6))
plt.bar(df['Nome'], df['Salário'])
plt.title('Salário por Funcionário')
plt.xlabel('Funcionário')
plt.ylabel('Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Bônus por Funcionário
plt.figure(figsize=(10, 6))
plt.bar(df['Nome'], df['Bônus'])
plt.title('Bônus por Funcionário (10% do Salário)')
plt.xlabel('Funcionário')
plt.ylabel('Bônus (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 3: Média de Salário por Título do Cargo
plt.figure(figsize=(10, 6))
plt.bar(agregado['Título do Cargo'], agregado['Média de Salário'])
plt.title('Média de Salário por Título do Cargo')
plt.xlabel('Título do Cargo')
plt.ylabel('Média de Salário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import seaborn as sns