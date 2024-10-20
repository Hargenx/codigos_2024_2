from controller.banco_controller import BancoDeDados
from model.dono import Dono


class DonoController:
    def __init__(self):
        self.bd = BancoDeDados()
        self.bd.conectar()

    def cadastrar_dono(self, nome, email, senha):
        dono_existente = self.bd.buscar_dono_por_email(
            email
        )  # Verifica se o email já existe
        if dono_existente:
            return False, "Dono já cadastrado"
        else:
            novo_dono = Dono(nome=nome, email=email, senha=senha)
            self.bd.inserir_dono(novo_dono)
            return True, "Cadastro realizado com sucesso"

    def realizar_login(self, email, senha):
        dono = self.bd.buscar_dono_por_email(email)
        if dono and dono.senha == senha:
            return True, "Login realizado com sucesso"
        return False, "Email ou senha incorretos"

    def fechar_conexao(self):
        self.bd.fechar_conexao()
