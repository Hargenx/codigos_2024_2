while True:
    print("R - Residência\nC - Comercio\nI - Indústria\nS - Sair")
    tipo_instalacao = input("Digite o tipo de instalação (R, C, I, S): ").upper()
    if tipo_instalacao == 'S':
        break
    faixa_kwh = input("Digite a faixa de kwh consumida (500, 1000, 5000): ")
    match tipo_instalacao:
        case 'R':
            if int(faixa_kwh) <= 500:
                preco = int(faixa_kwh) * 0.40
            else:
                preco = int(faixa_kwh) * 0.65
            print(f"O valor a pagar é: R$ {preco:.2f}")
        case 'C':
            if int(faixa_kwh) <= 1000:
                preco = int(faixa_kwh) * 0.55
            else:
                preco = int(faixa_kwh) * 0.60
            print(f"O valor a pagar é: R$ {preco:.2f}")
        case 'I':
            if int(faixa_kwh) <= 5000:
                preco = int(faixa_kwh) * 0.55
            else:
                preco = int(faixa_kwh) * 0.60
            print(f"O valor a pagar é: R$ {preco:.2f}")
        case 'S':
            break
        case _:
            print("Tipo de instalação inválida. Tente novamente.")
            continue


