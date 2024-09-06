import os

# Define o caminho para o arquivo CSV
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(diretorio_atual, "alunos.csv")


def carregar_dados() -> dict:
    """Carrega os dados do arquivo CSV, se existir; caso contrário, retorna um dicionário vazio."""
    if os.path.exists(diretorio):
        with open(diretorio, "r") as arquivo:
            linhas = arquivo.readlines()
        return {
            nome: float(nota)
            for nome, nota in (linha.strip().split(",") for linha in linhas)
        }
    return {}


def salvar_dados(dados: dict) -> bool:
    """Salva o dicionário de dados no arquivo CSV."""
    try:
        with open(diretorio, "w") as arquivo:
            for nome, nota in dados.items():
                arquivo.write(f"{nome},{nota}\n")
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")
        return False


def cadastrar_alunos(nome: str, nota: float) -> bool:
    """
    Cadastra um aluno no arquivo CSV.

    args: nome: o nome do aluno, nota: a nota do aluno
    retorno: True se o aluno foi cadastrado com sucesso, False caso contrário
    """
    try:
        with open(diretorio, "a") as arquivo:
            arquivo.write(f"{nome},{nota}\n")  # Usando vírgula como separador
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o aluno: {e}")
        return False


def ler_alunos() -> list:
    """
    Lê todos os alunos do arquivo CSV.

    args: None
    retorno: uma lista contendo todas as linhas do arquivo
    """
    if os.path.exists(diretorio):
        try:
            with open(diretorio, "r") as arquivo:
                linhas = arquivo.readlines()
            return linhas
        except Exception as e:
            print(f"Ocorreu um erro ao ler os alunos: {e}")
            return []
    else:
        print(f"O arquivo '{diretorio}' não existe.")
        return []


def ler_aluno(nome: str) -> str:
    """
    Lê um aluno específico do arquivo CSV.
    args: nome: o nome do aluno
    retorno: uma string contendo a linha do aluno ou mensagem de não encontrado
    """
    if os.path.exists(diretorio):
        try:
            with open(diretorio, "r") as arquivo:
                for linha in arquivo:
                    if linha.startswith(nome + ","):
                        return (
                            linha.strip()
                        )  # Retorna a linha do aluno sem espaços extras
        except Exception as e:
            print(f"Ocorreu um erro ao ler o aluno: {e}")
    return "Aluno não encontrado."


def remover_aluno(nome: str) -> bool:
    """
    Remove um aluno específico do arquivo CSV.
    args: nome: o nome do aluno
    retorno: True se o aluno foi removido com sucesso, False caso contrário
    """
    try:
        if os.path.exists(diretorio):
            with open(diretorio, "r") as arquivo:
                linhas = arquivo.readlines()
            with open(diretorio, "w") as arquivo:
                for linha in linhas:
                    if not linha.startswith(nome + ","):
                        arquivo.write(linha)
            return True
        else:
            print(f"O arquivo '{diretorio}' não existe.")
            return False
    except Exception as e:
        print(f"Ocorreu um erro ao remover o aluno: {e}")
        return False


def alterar_nota_aluno(nome: str, nova_nota: float) -> bool:
    """
    Altera a nota de um aluno específico no arquivo CSV.

    args: nome: o nome do aluno, nova_nota: a nova nota do aluno
    retorno: True se a nota foi alterada com sucesso, False caso contrário
    """
    encontrou = False
    try:
        if os.path.exists(diretorio):
            with open(diretorio, "r") as arquivo:
                linhas = arquivo.readlines()
            with open(diretorio, "w") as arquivo:
                for linha in linhas:
                    if linha.startswith(nome + ","):
                        arquivo.write(f"{nome},{nova_nota}\n")
                        encontrou = True
                    else:
                        arquivo.write(linha)
            return encontrou
        else:
            print(f"O arquivo '{diretorio}' não existe.")
            return False
    except Exception as e:
        print(f"Ocorreu um erro ao alterar a nota do aluno: {e}")
        return False


if __name__ == "__main__":
    print(cadastrar_alunos("Raphael", 10.0))
    print(ler_aluno("Raphael"))
    print(ler_alunos())
    print(remover_aluno("Raphael"))
    print(ler_alunos())
    print(cadastrar_alunos("Raphael", 10.0))
    print(alterar_nota_aluno("Raphael", 9.5))
    print(ler_alunos())
