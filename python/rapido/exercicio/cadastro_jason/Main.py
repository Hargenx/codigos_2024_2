import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(diretorio_atual, "alunos.json")

def carregar_dados() -> dict:
    """Carrega os dados do arquivo JSON, se existir; caso contrário, retorna um dicionário vazio."""
    if os.path.exists(diretorio):
        with open(diretorio, "r") as arquivo:
            return json.load(arquivo)
    return {}


def salvar_dados(dados: dict) -> bool:
    """Salva o dicionário de dados no arquivo JSON."""
    with open(diretorio, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    return True


def cadastrar_alunos(nome: str, nota: float) -> bool:
    """
    Cadastra um aluno no arquivo JSON.

    args: nome: o nome do aluno, nota: a nota do aluno
    retorno: True se o aluno foi cadastrado com sucesso, False caso contrário
    """
    dados = carregar_dados()
    dados[nome] = nota
    salvar_dados(dados)
    return True


def ler_alunos() -> list:
    """
    Lê todos os alunos do arquivo JSON.

    args: None
    retorno: uma lista de strings com todos os alunos e suas notas
    """
    dados = carregar_dados()
    return [f"{nome}: {nota}" for nome, nota in dados.items()]


def ler_aluno(nome: str) -> str:
    """
    Lê um aluno específico do arquivo JSON.

    args: nome: o nome do aluno
    retorno: uma string contendo o nome e a nota do aluno
    """
    dados = carregar_dados()
    return f"{nome}: {dados.get(nome, 'Aluno não encontrado')}"


def remover_aluno(nome: str) -> bool:
    """
    Remove um aluno específico do arquivo JSON.

    args: nome: o nome do aluno
    retorno: True se o aluno foi removido com sucesso, False caso contrário
    """
    dados = carregar_dados()
    if nome in dados:
        del dados[nome]
        salvar_dados(dados)
        return True
    return False


def alterar_nota_aluno(nome: str, nova_nota: float) -> bool:
    """
    Altera a nota de um aluno específico no arquivo JSON.

    args: nome: o nome do aluno, nova_nota: a nova nota do aluno
    retorno: True se o aluno foi alterado com sucesso, False caso contrário
    """
    dados = carregar_dados()
    if nome in dados:
        dados[nome] = nova_nota
        salvar_dados(dados)
        return True
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
