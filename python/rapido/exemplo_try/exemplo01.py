import pickle
import os

# Define o caminho para o arquivo CSV
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(diretorio_atual, "dados.bin")

dados = {"nome": "Raphael", "idade": 40, "profissão": "Desenvolvedor"}

try:
    with open(diretorio, "wb") as salva_binario:
        pickle.dump(dados, salva_binario)
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao salvar os dados: {e}")

try:
    with open(diretorio, "rb") as carrega_binario:
        dados_carregados = pickle.load(carrega_binario)
    print("Dados carregados com sucesso:", dados_carregados)
except Exception as e:
    print(f"Ocorreu um erro ao carregar os dados: {e}")
