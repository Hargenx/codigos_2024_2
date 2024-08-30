# https://docs.python.org/3/library/functions.html


lista = ['Raphael', 2, '3', 4, 5, 'O', 7, 8, 9.8, 10]


print('Rapha' in lista)

print(10 not in lista)

# exemplo de uso de all
'''for i in range(1, 11):
    print(i, all(range(1, i)))

print(all([1, 2, 3, 4, 5])) # True - todos os valores sao verdadeiros

print(all([1, 2, 3, 4, 0])) # False - pelo menos um valor é falso

print(all([])) # True - lista vazia'''

# Exemplo 1: Verificando se todos os números em uma lista são positivos
numeros = [1, 2, 3, 4, 5]
todos_positivos = all(num > 0 for num in numeros)
print(f"Verifica se positivos: {todos_positivos}")  # Saída: True

# Exemplo 2: Verificando se todas as strings em uma lista têm mais de 3 caracteres
palavras = ["Carol", "Raphael", "Vinicius"]
todas_longas = all(len(palavra) > 3 for palavra in palavras)
print(f"Verifica se todos longos: {todas_longas}")  # Saída: True

# Exemplo 3: Usando uma lista que contém um valor falso
numeros_mistos = [1, 2, 0, 4, 5]
todos_positivos = all(num > 0 for num in numeros_mistos)
print(f"Verifica se positivos: {todos_positivos}")  # Saída: False


# exemplo de uso de any
for i in range(1, 11):
    print(i, any(range(1, i)))
