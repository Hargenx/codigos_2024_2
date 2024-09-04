def calcular_area(largura: float, comprimento: float) -> float:
    """
    Calcula a área de uma sala retangular.

    :param largura: Largura da sala
    :param comprimento: Comprimento da sala
    :return: Área da sala
    """
    return largura * comprimento


def calcular_perimetro(largura: float, comprimento: float) -> float:
    """
    Calcula o perímetro de uma sala retangular.

    :param largura: Largura da sala
    :param comprimento: Comprimento da sala
    :return: Perímetro da sala
    """
    return 2 * (largura + comprimento)


def main():
    # Solicita as dimensões da sala ao usuário
    largura = float(input("Digite a largura da sala: "))
    comprimento = float(input("Digite o comprimento da sala: "))

    # Calcula a área e o perímetro
    area = calcular_area(largura, comprimento)
    perimetro = calcular_perimetro(largura, comprimento)

    # Exibe os resultados
    print(f"A área da sala é: {area} metros quadrados")
    print(f"O perímetro da sala é: {perimetro} metros")


if __name__ == "__main__":
    main()
