import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from controller.veiculo import Veiculo 

class CadastroVeiculoApp:
    def __init__(self, root, banco_dados):
        self.root = root
        self.banco = banco_dados
        self.root.title("Cadastro de Veículo")
        self.root.geometry("400x400")

        # Definir o fundo da janela
        self.root.configure(bg='#2c3e50')

        # Centralizar os widgets
        self.frame = tk.Frame(root, bg='#34495e')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Título
        self.label_title = tk.Label(self.frame, text="CADASTRAR VEÍCULO", font=("Arial", 18, "bold"), bg='#34495e', fg='white')
        self.label_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Campo para a Placa do Veículo
        self.label_placa = tk.Label(self.frame, text="Placa:", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_placa.grid(row=1, column=0, padx=10, pady=10)
        self.entry_placa = tk.Entry(self.frame, font=("Arial", 14))
        self.entry_placa.grid(row=1, column=1, padx=10, pady=10)

        # Campo para a Cor do Veículo
        self.label_cor = tk.Label(self.frame, text="Cor:", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_cor.grid(row=2, column=0, padx=10, pady=10)
        self.entry_cor = tk.Entry(self.frame, font=("Arial", 14))
        self.entry_cor.grid(row=2, column=1, padx=10, pady=10)

        # Combobox para selecionar a Marca do Veículo
        self.label_marca = tk.Label(self.frame, text="Marca:", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_marca.grid(row=3, column=0, padx=10, pady=10)

        self.combobox_marca = ttk.Combobox(self.frame, font=("Arial", 14))
        self.combobox_marca.grid(row=3, column=1, padx=10, pady=10)

        # Preencher o Combobox com marcas do banco de dados
        self.preencher_combobox_marcas()

        # Botão para Cadastrar o Veículo
        self.btn_cadastrar = tk.Button(self.frame, text="Cadastrar Veículo", font=("Arial", 14), command=self.cadastrar_veiculo, bg='#1abc9c', fg='white', bd=0, width=20)
        self.btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=20)

    def preencher_combobox_marcas(self):
        # Preencher o combobox com marcas obtidas do banco de dados
        marcas = self.banco.buscar_todas_marcas()
        nomes_marcas = [marca.nome for marca in marcas]
        self.combobox_marca['values'] = nomes_marcas
        self.combobox_marca.current(0)  # Seleciona a primeira marca como padrão

    def cadastrar_veiculo(self):
        placa = self.entry_placa.get()
        cor = self.entry_cor.get()
        marca_nome = self.combobox_marca.get()

        # Verificar se todos os campos foram preenchidos
        if placa and cor and marca_nome:
            try:
                # Buscar a marca selecionada
                marca = next((marca for marca in self.banco.buscar_todas_marcas() if marca.nome == marca_nome), None)

                if marca:
                    veiculo = Veiculo(placa=placa, cor=cor, marca=marca, propietario=None)  # Aqui, o proprietário ainda é None
                    self.banco.inserir_veiculo(veiculo)
                    messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
                else:
                    messagebox.showerror("Erro", "Marca não encontrada.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar veículo: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
