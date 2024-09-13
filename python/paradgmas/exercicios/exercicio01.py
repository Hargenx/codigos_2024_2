def verificar_multa(velocidade: float) -> str:
    limite_velocidade = 80  # Limite de velocidade em km/h
    multa_base = 100        # Multa fixa
    valor_por_km = 15       # Valor cobrado por km acima do limite

    if velocidade > limite_velocidade:
        km_acima = velocidade - limite_velocidade
        valor_multa = multa_base + (km_acima * valor_por_km)
        print(f"Você foi multado! O valor da multa é de R$ {valor_multa:.2f}.")
    else:
        print("Você está dentro do limite de velocidade. Nenhuma multa aplicada.")

velocidade = float(input("Digite a velocidade do carro (km/h): "))
resultado = verificar_multa(velocidade)
print(resultado)
