from controller.pessoa import Pessoa
from controller.veiculo import Veiculo
from controller.marca import Marca
from model.banco import BancoDeDados


class MotoristaController:
    def __init__(self):
        self.banco = BancoDeDados()
        self.banco.conectar()
        self.banco.criar_tabelas()

    def cadastrar_motorista(
        self,
        cpf,
        nome,
        nascimento,
        oculos,
        placa,
        cor,
        marca_id,
        marca_nome,
        marca_sigla,
    ):
        # Criar as instâncias de Pessoa, Marca e Veículo
        pessoa = Pessoa(cpf, nome, nascimento, oculos)
        marca = Marca(marca_id, marca_nome, marca_sigla)
        veiculo = Veiculo(placa, cor, pessoa, marca)

        # Inserir no banco de dados
        self.banco.inserir_pessoa(pessoa)
        self.banco.inserir_marca(marca)
        self.banco.inserir_veiculo(veiculo)

    def atualizar_motorista(self, cpf, nome, nascimento, oculos):
        pessoa = Pessoa(cpf, nome, nascimento, oculos)
        self.banco.atualizar_pessoa(pessoa)

    def buscar_motorista_por_cpf(self, cpf):
        return self.banco.buscar_pessoa_por_cpf(cpf)

    def buscar_todos_motoristas(self):
        return self.banco.buscar_todas_pessoas()

    def deletar_motorista(self, cpf):
        pessoa = self.banco.buscar_pessoa_por_cpf(cpf)
        if pessoa:
            self.banco.apagar_pessoa(pessoa)

    # Outros métodos para veículos e marcas podem ser adicionados aqui...
