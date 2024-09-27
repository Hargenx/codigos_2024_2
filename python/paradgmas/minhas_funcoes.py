def exemplo_de_aula_1(valor1: int, valor2: float) -> list:
    for _ in range(10):
        lista = [valor1 + valor2 * i for i in range(10)]
    return lista

def exemplo_de_aula_2() -> str:
    import math
    ceil = math.ceil(math.pi)
    floor = math.floor(math.pi)
    sqrt = math.sqrt(2)
    fat = math.factorial(4)
    fabs = math.fabs(-45.2)
    return f"PI: {math.pi}\nE: {math.e}\nPI de graus: {math.sin(math.pi)}\nCeil: {ceil}\nFloor: {floor}\nSqrt: {sqrt}\nFatorial de 4: {fat}\nValor absoluto de -45.2: {fabs}"


def exemplo_de_aula_3() -> str:
    import random

    while True:
        num = int(input("Quantas vezes quer jogar? "))
        if num == 1:
            num = random.randint(0, 1)
            print(num)
        else:
            break


if __name__ == "__main__":
    print(f"Executando o exemplo 1: \n{exemplo_de_aula_1(1, 2)}\n\n")
    print(f"Executando o exemplo 2: \n{exemplo_de_aula_2()}\n\n")
    print(f"Executando o exemplo 3: \n{exemplo_de_aula_3()}\n\n")