import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cria um conjunto de dados fictício de vendas por produto
produtos = ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E"]
vendas = [5000, 7000, 3000, 6000, 8000]

# Cria um DataFrame simples
dados_vendas = pd.DataFrame({"Produto": produtos, "Vendas": vendas})

# Configura estilo do Seaborn (opcional)
sns.set(style="whitegrid")

# Criar um gráfico de barras das vendas por produto
plt.figure(figsize=(10, 6))
sns.barplot(x="Vendas", y="Produto", data=dados_vendas, hue="Produto", palette="viridis", legend=False)
plt.xlabel('Vendas')
plt.ylabel('Produto')
plt.title('Vendas por Produto')
plt.show()
