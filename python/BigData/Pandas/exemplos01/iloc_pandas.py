import pandas as pd

# Criando um DataFrame exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Cargo': ['Gerente', 'Analista', 'Assistente', 'Diretor'],
    'Salário': [5000, 3500, 2000, 6000]
}

df = pd.DataFrame(data)
print(df)
# Usando iloc para selecionar a primeira e segunda linha e as colunas "Nome" e "Salário"
resultado_iloc = df.iloc[0:2, [0, 2]]
print(resultado_iloc)

# Usando loc para selecionar o funcionário "Carlos" e projetar as colunas "Nome" e "Salário"
resultado_loc = df.loc[df['Nome'] == 'Carlos', ['Nome', 'Salário']]
print(resultado_loc)

# Usando query para selecionar funcionários com salário maior que 4000
resultado_query = df.query('Salário > 4000')
print(resultado_query)
