import os
import re
from datetime import datetime

# Define o caminho para o arquivo de log
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_log = os.path.join(diretorio_atual, "server_logs.txt")


def processar_logs(caminho_arquivo: str) -> dict:
    """
    Processa o arquivo de log e extrai o número de solicitações bem-sucedidas e falhas.

    args: caminho_arquivo: o caminho para o arquivo de log
    retorno: um dicionário com o número de solicitações bem-sucedidas e falhas
    """
    sucesso = 0
    falhas = 0

    try:
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    match = re.match(
                        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (\d{3})", linha
                    )
                    if match:
                        status_codigo = int(match.group(1))
                        if status_codigo == 200:
                            sucesso += 1
                        elif 400 <= status_codigo < 600:
                            falhas += 1
        else:
            print(f"O arquivo de log '{caminho_arquivo}' não existe.")

    except Exception as e:
        print(f"Ocorreu um erro ao processar os logs: {e}")

    return {"sucesso": sucesso, "falhas": falhas}


if __name__ == "__main__":
    resultados = processar_logs(arquivo_log)
    print(f"Número de solicitações bem-sucedidas: {resultados['sucesso']}")
    print(f"Número de falhas: {resultados['falhas']}")
