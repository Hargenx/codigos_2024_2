def calcular_preco_energia(kwh_consumida, tipo_instalacao):
    match tipo_instalacao:
        case 'R':
            # Residencial
            if kwh_consumida <= 500:
                preco = kwh_consumida * 0.40
            else:
                preco = kwh_consumida * 0.65
        case 'C':
            # Comercial
            if kwh_consumida <= 1000:
                preco = kwh_consumida * 0.55
            else:
                preco = kwh_consumida * 0.60
        case 'I':
            # Industrial
            if kwh_consumida <= 5000:
                preco = kwh_consumida * 0.55
            else:
                preco = kwh_consumida * 0.60
        case _:
            # Tipo de instalação inválido
            return "Tipo de instalação inválido. Use 'R' para residências, 'C' para comércios ou 'I' para indústrias."
    
    return f"O preço a pagar é: R$ {preco:.2f}"

# Exemplo de uso
kwh_consumida = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R, C, I): ").upper()

resultado = calcular_preco_energia(kwh_consumida, tipo_instalacao)
print(resultado)
