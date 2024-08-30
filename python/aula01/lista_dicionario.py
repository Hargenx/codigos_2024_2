class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


meu_carro = Carro("Toyota", "Corolla", 2020)
print(meu_carro.marca, meu_carro.modelo, meu_carro.ano)

carros = [
    Carro("Toyota", "Corolla", 2020),
    Carro("Honda", "Civic", 2018),
    Carro("Ford", "Mustang", 2021),
]

for carro in carros:
    print(carro.modelo)
