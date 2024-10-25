def conta_letras(palavra: str, letra: str) -> int:
    soma = 0
    for letras in palavra:
        if letras == letra:
            soma += 1
    return soma

def troca_valor(lista: list, v1: int, v2: int) -> list:
    for index, valor in enumerate(lista):
        if valor == v1:
            lista[index] = v2
    return lista 