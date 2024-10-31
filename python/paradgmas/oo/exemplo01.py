class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # Atributo público
        self.__idade = idade  # Atributo privado, acessível apenas dentro da classe
    
    # Método público para acessar o atributo privado
    def get_idade(self):
        return self.__idade
    
    # Método público para modificar o atributo privado
    def set_idade(self, nova_idade):
        if nova_idade > 0:  # Verifica se a idade é válida
            self.__idade = nova_idade
        else:
            print("Idade inválida!")

# Exemplo de uso
pessoa = Pessoa("Raphael", 40)
print(pessoa.nome)        # Acesso ao atributo público
print(pessoa.get_idade()) # Acesso ao atributo privado via método público

pessoa.set_idade(30)      # Modificando o atributo privado
print(pessoa.get_idade())

pessoa.set_idade(-5)      # Tentando modificar com valor inválido
