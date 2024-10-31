class Pessoas:
    def __init__(self, nome: str, idade: int) -> None:
        """Construtor da classe Pessoas.

        Args:
            nome (str): Nome da pessoa.
            idade (int): Idade da pessoa.
        
        Returns:
            None
        """
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self) -> None:
        """Método para exibir informacoes da pessoa.
        
        Args:
            None

        Returns:
            None
        """
        print("Informacoes da pessoa:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

    def atualizar_idade(self, nova_idade: int) -> None:
        """Método para atualizar a idade da pessoa.

        Args:
            nova_idade (int): Nova idade da pessoa.

        Returns:
            None
        """
        self.idade = nova_idade
        print(f"Idade atualizada para {self.idade}")

    def calcular_idade_em_dias(self) -> None:
        """Método para calcular a idade da pessoa em dias.

        Args:
            None

        Returns:
            None
        """
        print(f"Idade em dias: {self.idade * 365}")