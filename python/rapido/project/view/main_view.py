import tkinter as tk
from tkinter import messagebox
import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controller.dono_controller import DonoController
from controller.dono_controller import DonoController
from controller.veiculo_controller import VeiculoController
from controller.pessoa_controller import PessoaController


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento")
        self.geometry("400x300")
        self.centralizar_janela()

        self.create_widgets()
        self.dono_controller = DonoController()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        label_bem_vindo = tk.Label(
            self, text="Bem-vindo ao Sistema", font=("Arial", 16)
        )
        label_bem_vindo.pack(pady=10)

        btn_login = tk.Button(self, text="Login", command=self.abrir_login)
        btn_login.pack(pady=5)

        btn_cadastro = tk.Button(self, text="Cadastro", command=self.abrir_cadastro)
        btn_cadastro.pack(pady=5)

    def abrir_login(self):
        self.destroy()
        LoginView()

    def abrir_cadastro(self):
        self.destroy()
        CadastroView()


class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login de Dono")
        self.geometry("400x200")
        self.centralizar_janela()
        self.create_widgets()
        self.dono_controller = DonoController()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        tk.Label(self, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.pack(pady=5)

        btn_login = tk.Button(self, text="Login", command=self.realizar_login)
        btn_login.pack(pady=5)

    def realizar_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        sucesso, msg = self.dono_controller.realizar_login(email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.destroy()
            PrincipalView()
        else:
            messagebox.showerror("Erro", msg)


class CadastroView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Dono")
        self.geometry("400x300")
        self.centralizar_janela()
        self.create_widgets()
        self.dono_controller = DonoController()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        tk.Label(self, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.pack(pady=5)

        btn_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_dono)
        btn_cadastrar.pack(pady=10)

    def cadastrar_dono(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        sucesso, msg = self.dono_controller.cadastrar_dono(nome, email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.destroy()
            Application()
        else:
            messagebox.showerror("Erro", msg)


class PrincipalView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Principal")
        self.geometry("600x400")
        self.centralizar_janela()
        self.create_widgets()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        label_bem_vindo = tk.Label(
            self, text="Bem-vindo ao Sistema Principal", font=("Arial", 16)
        )
        label_bem_vindo.pack(pady=10)

        btn_cadastrar_veiculo = tk.Button(
            self, text="Cadastrar Veículo", command=self.abrir_cadastro_veiculo
        )
        btn_cadastrar_veiculo.pack(pady=10)

        btn_cadastrar_motorista = tk.Button(
            self, text="Cadastrar Motorista", command=self.abrir_cadastro_motorista
        )
        btn_cadastrar_motorista.pack(pady=10)

    def abrir_cadastro_veiculo(self):
        CadastroVeiculoView()

    def abrir_cadastro_motorista(self):
        CadastroMotoristaView()


class CadastroVeiculoView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Veículo")
        self.geometry("400x300")
        self.centralizar_janela()
        self.create_widgets()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        tk.Label(self, text="Placa:").pack(pady=5)
        self.entry_placa = tk.Entry(self)
        self.entry_placa.pack(pady=5)

        tk.Label(self, text="Cor:").pack(pady=5)
        self.entry_cor = tk.Entry(self)
        self.entry_cor.pack(pady=5)

        tk.Label(self, text="CPF do Proprietário:").pack(pady=5)
        self.entry_cpf_proprietario = tk.Entry(self)
        self.entry_cpf_proprietario.pack(pady=5)

        tk.Label(self, text="ID da Marca:").pack(pady=5)
        self.entry_id_marca = tk.Entry(self)
        self.entry_id_marca.pack(pady=5)

        btn_cadastrar = tk.Button(
            self, text="Cadastrar", command=self.cadastrar_veiculo
        )
        btn_cadastrar.pack(pady=10)

    def cadastrar_veiculo(self):
        placa = self.entry_placa.get()
        cor = self.entry_cor.get()
        cpf_proprietario = self.entry_cpf_proprietario.get()
        id_marca = self.entry_id_marca.get()

        veiculo_controller = VeiculoController()
        veiculo_controller.cadastrar_veiculo(placa, cor, cpf_proprietario, id_marca)
        messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
        self.destroy()


class CadastroMotoristaView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Motorista")
        self.geometry("400x300")
        self.centralizar_janela()
        self.create_widgets()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        tk.Label(self, text="Nome do Motorista:").pack(pady=5)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="CPF:").pack(pady=5)
        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.pack(pady=5)

        tk.Label(self, text="Data de Nascimento (AAAA-MM-DD):").pack(pady=5)
        self.entry_nascimento = tk.Entry(self)
        self.entry_nascimento.pack(pady=5)

        tk.Label(self, text="Usa Óculos? (True/False):").pack(pady=5)
        self.entry_oculos = tk.Entry(self)
        self.entry_oculos.pack(pady=5)

        btn_cadastrar = tk.Button(
            self, text="Cadastrar", command=self.cadastrar_motorista
        )
        btn_cadastrar.pack(pady=10)

    def cadastrar_motorista(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        nascimento = self.entry_nascimento.get()
        oculos = self.entry_oculos.get()

        pessoa_controller = PessoaController()
        pessoa_controller.cadastrar_pessoa(cpf, nome, nascimento, oculos)
        messagebox.showinfo("Sucesso", "Motorista cadastrado com sucesso!")
        self.destroy()


# Iniciar a aplicação
if __name__ == "__main__":
    app = Application()
    app.mainloop()
