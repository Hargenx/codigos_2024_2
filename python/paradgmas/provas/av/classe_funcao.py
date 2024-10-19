#Carlos (Paradigma Funcional):
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print(soma)
#------------------------------------
#Ana (Paradigma Orientado a Objetos):
class SomaLista:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcular_soma(self):
        return sum(self.numeros)

numeros = [1, 2, 3, 4, 5]
soma_lista = SomaLista(numeros)
print(soma_lista.calcular_soma())
#-----------------------------------
#João (Paradigma Procedural):
def calcular_soma(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

numeros = [1, 2, 3, 4, 5]
soma = calcular_soma(numeros)
print(soma)