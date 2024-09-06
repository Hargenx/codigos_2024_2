import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio = os.path.join(diretorio_atual, "catalogo_jogos.json")

def carregar_dados() -> dict:
    """Carrega os dados do arquivo JSON, se existir; caso contrário, retorna um dicionário vazio."""
    if os.path.exists("diretorio"):
        with open(diretorio, "r") as arquivo:
            return json.load(arquivo)
    return {}


def salvar_dados(dados: dict) -> bool:
    """Salva o dicionário de dados no arquivo JSON."""
    with open(diretorio, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    return True


def cadastrar_jogo(
    nome: str, plataforma: str, capa: str, nota: float, completado: bool, screens: list
) -> bool:
    """
    Cadastra um jogo no catálogo.

    args: nome: o nome do jogo, plataforma: a plataforma do jogo, capa: a imagem de capa, nota: a nota do jogo,
          completado: se o jogo foi completado ou não, screens: lista de imagens de tela
    retorno: True se o jogo foi cadastrado com sucesso, False caso contrário
    """
    dados = carregar_dados()
    dados[nome] = {
        "plataforma": plataforma,
        "capa": capa,
        "nota": nota,
        "completado": completado,
        "screens": screens,
    }
    salvar_dados(dados)
    return True


def ler_jogos() -> list:
    """
    Lê todos os jogos do catálogo.

    args: None
    retorno: uma lista de strings com todos os jogos e suas informações
    """
    dados = carregar_dados()
    return [f"{nome}: {info}" for nome, info in dados.items()]


def ler_jogo(nome: str) -> str:
    """
    Lê um jogo específico do catálogo.

    args: nome: o nome do jogo
    retorno: uma string contendo todas as informações do jogo
    """
    dados = carregar_dados()
    return dados.get(nome, "Jogo não encontrado.")


def remover_jogo(nome: str) -> bool:
    """
    Remove um jogo específico do catálogo.

    args: nome: o nome do jogo
    retorno: True se o jogo foi removido com sucesso, False caso contrário
    """
    dados = carregar_dados()
    if nome in dados:
        del dados[nome]
        salvar_dados(dados)
        return True
    return False


def alterar_jogo(
    nome: str,
    plataforma: str = None,
    capa: str = None,
    nota: float = None,
    completado: bool = None,
    screens: list = None,
) -> bool:
    """
    Altera as informações de um jogo específico no catálogo.

    args: nome: o nome do jogo, plataforma: a plataforma do jogo, capa: a imagem de capa,
          nota: a nota do jogo, completado: se o jogo foi completado ou não, screens: lista de imagens de tela
    retorno: True se o jogo foi alterado com sucesso, False caso contrário
    """
    dados = carregar_dados()
    if nome in dados:
        if plataforma is not None:
            dados[nome]["plataforma"] = plataforma
        if capa is not None:
            dados[nome]["capa"] = capa
        if nota is not None:
            dados[nome]["nota"] = nota
        if completado is not None:
            dados[nome]["completado"] = completado
        if screens is not None:
            dados[nome]["screens"] = screens
        salvar_dados(dados)
        return True
    return False


if __name__ == "__main__":
    print(
        cadastrar_jogo(
            "The Legend of Zelda: Breath of the Wild",
            "Nintendo Switch",
            "capa_zelda.png",
            9.8,
            True,
            ["screen1.png", "screen2.png"],
        )
    )
    print(ler_jogo("The Legend of Zelda: Breath of the Wild"))
    print(ler_jogos())
    print(remover_jogo("The Legend of Zelda: Breath of the Wild"))
    print(ler_jogos())
    print(
        cadastrar_jogo(
            "The Legend of Zelda: Breath of the Wild",
            "Nintendo Switch",
            "capa_zelda.png",
            9.8,
            True,
            ["screen1.png", "screen2.png"],
        )
    )
    print(alterar_jogo("The Legend of Zelda: Breath of the Wild", nota=10.0))
    print(ler_jogos())
