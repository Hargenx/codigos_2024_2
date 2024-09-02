from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int

    def exibir_informacoes(self) -> str:
        return (
            f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}"
        )


produto1 = Produto("Caneta", 1.50, 100)
print(produto1.exibir_informacoes())
