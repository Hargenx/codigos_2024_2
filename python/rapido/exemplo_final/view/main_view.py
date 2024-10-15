import tkinter as tk
from tkinter import messagebox
from model.banco import BancoDeDados
from view.cadastrar_veiculo_view import CadastroVeiculoApp

class MainApp:
    def __init__(self, root, banco):
        self.root = root
        self.banco = banco  # Atribui o banco de dados recebido

        self.root.title("Cadastro de Motoristas e Veículos")
        self.root.geometry("400x600")

        # Definir o fundo da janela
        self.root.configure(bg='#2c3e50')

        # Centralizar os widgets
        self.frame = tk.Frame(root, bg='#34495e')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Título
        self.label_title = tk.Label(self.frame, text="MENU PRINCIPAL", font=("Arial", 24, "bold"), bg='#34495e', fg='white')
        self.label_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Botões para cadastrar motorista e veículo
        self.btn_cadastrar_motorista = tk.Button(self.frame, text="Cadastrar Motorista", font=("Arial", 14), command=self.cadastrar_motorista, bg='#1abc9c', fg='white', bd=0, width=20)
        self.btn_cadastrar_motorista.grid(row=1, column=0, columnspan=2, pady=10)

        self.btn_cadastrar_veiculo = tk.Button(self.frame, text="Cadastrar Veículo", font=("Arial", 14), command=self.cadastrar_veiculo, bg='#1abc9c', fg='white', bd=0, width=20)
        self.btn_cadastrar_veiculo.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de veículos cadastrados
        self.label_veiculos = tk.Label(self.frame, text="Veículos Cadastrados:", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_veiculos.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox_veiculos = tk.Listbox(self.frame, font=("Arial", 12), width=40, height=10)
        self.listbox_veiculos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Preencher com dados fictícios (substitua pela lógica real)
        self.atualizar_lista_veiculos()

    def cadastrar_motorista(self):
        messagebox.showinfo("Cadastrar", "Redirecionar para tela de cadastro de motorista")

    def cadastrar_veiculo(self):
        root = tk.Toplevel()  # Abre uma nova janela
        app = CadastroVeiculoApp(root, self.banco)  # Agora usamos self.banco em vez de self.controller.banco
        root.mainloop()

    def atualizar_lista_veiculos(self):
        # Adicionar veículos fictícios (essa função deve ser ajustada com os dados reais)
        veiculos = ["Placa ABC1234 - Ford - Com Motorista", "Placa XYZ9876 - Honda - Sem Motorista"]
        for veiculo in veiculos:
            self.listbox_veiculos.insert(tk.END, veiculo)
