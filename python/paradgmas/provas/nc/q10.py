def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def calcula_resultado(a, b):
    return fatorial(a) + b


a = 4
b = 3
resultado = calcula_resultado(a, b)
print(f"O resultado é: {resultado}")