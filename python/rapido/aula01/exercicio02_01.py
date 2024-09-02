def calcular_valor_em_reais(quantidade_dolares: float, cotacao_dolar: float) -> float:
    return quantidade_dolares * cotacao_dolar


def main():
    while True:
        print("\nMenu:")
        print("1. Calcular valor em reais")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                quantidade_dolares = float(
                    input("Digite a quantidade de dólares guardados no cofre: ")
                )
                cotacao_dolar = float(input("Digite a cotação do dólar hoje: "))
                valor_em_reais = calcular_valor_em_reais(
                    quantidade_dolares, cotacao_dolar
                )
                print(f"O valor correspondente em reais é: R$ {valor_em_reais:.2f}")
            case 0:
                print("Saindo...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
