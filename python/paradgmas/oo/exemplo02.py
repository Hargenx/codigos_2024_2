class Pessoa:
    def __init__(self, nome, idade, time):
        self.nome = nome       # Atributo público
        self.__idade = idade
        self._time = time    # Atributo protegido

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Time: {self._time}, Idade: {self.__idade}"

# Classe que herda de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, time, salario):
        super().__init__(nome, idade, time)
        self.salario = salario

    # Método para exibir todas as informações
    def exibir_detalhes(self):
        return f"{self.exibir_informacoes()}, Salário: {self.salario}"

# Exemplo de uso
funcionario = Funcionario("Raphael", 40, "Flamengo", 35000)
print(funcionario.exibir_detalhes())

# Acessando diretamente o atributo protegido
print(funcionario._time)  # Acesso permitido, mas desencorajado pela convenção
