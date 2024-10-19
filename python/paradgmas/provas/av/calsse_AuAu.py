class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        return "Este animal faz um som."

class Cachorro(Animal):
    def som(self):
        return "O cachorro late."

class Gato(Animal):
    def nada():
        pass

meu_cachorro = Cachorro("Rex")
print(meu_cachorro.som())
meu_gato = Gato('Miau')
print(meu_gato.som())