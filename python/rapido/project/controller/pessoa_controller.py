from controller.banco_controller import BancoDeDados
from model.pessoa import Pessoa


class PessoaController:
    def __init__(self):
        self.bd = BancoDeDados()
        self.bd.conectar()

    def cadastrar_pessoa(self, cpf, nome, nascimento, oculos):
        pessoa = Pessoa(cpf=cpf, nome=nome, nascimento=nascimento, oculos=oculos)
        self.bd.inserir_pessoa(pessoa)

    def fechar_conexao(self):
        self.bd.fechar_conexao()
