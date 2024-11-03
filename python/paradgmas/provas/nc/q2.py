x = 10


def funcao1():
    x = 20

    def funcao2():
        nonlocal x
        x = 30
        print(f"Valor de x dentro de funcao2: {x}")

    funcao2()
    print(f"Valor de x dentro de funcao1 após funcao2: {x}")


funcao1()
print(f"Valor de x no escopo global: {x}")
