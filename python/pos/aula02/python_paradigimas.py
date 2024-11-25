from functools import reduce

def uso_reduce(lista: list) -> int:
    '''
    Recebe uma lista de inteiros e retorna a soma de todos os elementos da lista.
    
    args: lista: uma lista de inteiros
    return: a soma de todos os elementos da lista
    '''
    return reduce(lambda x, y: x + y, lista)

def uso_map(lista: list) -> list:
    '''
    Recebe uma lista de inteiros e retorna uma nova lista com os quadrados dos elementos da lista.
    
    args: lista: uma lista de inteiros
    return: uma nova lista com os quadrados dos elementos da lista
    '''
    return list(map(lambda x: x**2, lista))

def uso_filter(lista: list) -> list:
    
    '''
    Recebe uma lista de inteiros e retorna uma nova lista com os elementos pares da lista.
    
    args: lista: uma lista de inteiros
    return: uma nova lista com os elementos pares da lista

    '''
    return list(filter(lambda x: x % 2 == 0, lista))


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]

    soma = uso_reduce(lista)  # Resultado: 15
    lista_quadrados = uso_map(lista)  # Resultado: [1, 4, 9, 16, 25]
    pares = uso_filter(lista)  # Resultado: [2, 4]
    print(f'Resultado do uso_reduce: {soma}\nResultado do uso_map: {lista_quadrados}\nResultado do uso_filter: {pares}')