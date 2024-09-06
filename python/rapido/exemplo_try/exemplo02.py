import os

# Obtém o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Nome dos arquivos de imagem
imagem_entrada_nome = os.path.join(diretorio_atual, "imagem_original.jpg")
imagem_saida_nome = os.path.join(diretorio_atual, "imagem_copia.jpg")

# Verificando se o arquivo de imagem de entrada está na pasta de execução
if os.path.exists(imagem_entrada_nome):
    try:
        with open(imagem_entrada_nome, "rb") as imagem_entrada:
            with open(imagem_saida_nome, "wb") as imagem_saida:
                imagem_saida.write(imagem_entrada.read())
        print("Imagem copiada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao copiar a imagem: {e}")
else:
    print(
        f"O arquivo de imagem '{imagem_entrada_nome}' não foi encontrado na pasta de execução."
    )
