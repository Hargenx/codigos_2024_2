def calcular_valor_em_reais(quantidade_dolares: float, cotacao_dolar: float) -> float:
    """
    Calcula o valor em reais com base na quantidade de dólares e na cotação do dólar.

    :param quantidade_dolares: Quantidade de dólares guardados no cofre
    :param cotacao_dolar: Cotação do dólar no dia
    :return: Valor correspondente em reais
    """
    return quantidade_dolares * cotacao_dolar


def main():
    # Solicita ao usuário a quantidade de dólares e a cotação do dólar
    quantidade_dolares = float(
        input("Digite a quantidade de dólares guardados no cofre: ")
    )
    cotacao_dolar = float(input("Digite a cotação do dólar hoje: "))

    # Calcula o valor em reais
    valor_em_reais = calcular_valor_em_reais(quantidade_dolares, cotacao_dolar)

    # Exibe o resultado
    print(f"O valor correspondente em reais é: R$ {valor_em_reais:.2f}")


if __name__ == "__main__":
    main()
