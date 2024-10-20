from controller.banco_controller import BancoDeDados
from model.veiculo import Veiculo


class VeiculoController:
    def __init__(self):
        self.bd = BancoDeDados()
        self.bd.conectar()

    def cadastrar_veiculo(self, placa, cor, cpf_proprietario, id_marca):
        veiculo = Veiculo(
            placa=placa, cor=cor, cpf_proprietario=cpf_proprietario, id_marca=id_marca
        )
        self.bd.inserir_veiculo(veiculo)

    def fechar_conexao(self):
        self.bd.fechar_conexao()
