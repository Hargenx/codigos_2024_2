import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Para o Combobox
from controller.motorista_controller import MotoristaController


class MotoristaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Motoristas")
        self.controller = MotoristaController()

        # Componentes da interface
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.grid(row=1, column=0)
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.grid(row=1, column=1)

        self.label_nascimento = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):")
        self.label_nascimento.grid(row=2, column=0)
        self.entry_nascimento = tk.Entry(root)
        self.entry_nascimento.grid(row=2, column=1)

        # Checkbox para "Usa óculos"
        self.oculos_var = tk.BooleanVar()  # Variável associada ao checkbox
        self.check_oculos = tk.Checkbutton(
            root, text="Usa óculos?", variable=self.oculos_var
        )
        self.check_oculos.grid(row=3, column=1)

        self.label_placa = tk.Label(root, text="Placa do Veículo:")
        self.label_placa.grid(row=4, column=0)
        self.entry_placa = tk.Entry(root)
        self.entry_placa.grid(row=4, column=1)

        self.label_cor = tk.Label(root, text="Cor do Veículo:")
        self.label_cor.grid(row=5, column=0)
        self.entry_cor = tk.Entry(root)
        self.entry_cor.grid(row=5, column=1)

        # Combobox para selecionar a marca do veículo
        self.label_marca = tk.Label(root, text="Marca do Veículo:")
        self.label_marca.grid(row=6, column=0)
        self.combobox_marca = ttk.Combobox(
            root, values=["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"]
        )
        self.combobox_marca.grid(row=6, column=1)
        self.combobox_marca.current(0)  # Define o valor padrão para "Toyota"

        # Botão para cadastrar motorista
        self.btn_cadastrar = tk.Button(
            root, text="Cadastrar", command=self.cadastrar_motorista
        )
        self.btn_cadastrar.grid(row=7, column=0, columnspan=2)

    def cadastrar_motorista(self):
        try:
            cpf = int(self.entry_cpf.get())
            nome = self.entry_nome.get()
            nascimento = self.entry_nascimento.get()
            oculos = self.oculos_var.get()  # Pega o valor booleano do checkbox
            placa = self.entry_placa.get()
            cor = self.entry_cor.get()
            marca_nome = (
                self.combobox_marca.get()
            )  # Pega a marca selecionada no combobox

            # Definindo um ID de marca (pode ser automático, mas estou usando uma lógica simples para fins de demonstração)
            marca_id = self.combobox_marca.current() + 1  # ID baseado na seleção

            # Como o campo sigla da marca não está sendo usado no combobox, vamos criar uma sigla automática (opcional)
            marca_sigla = marca_nome[:3].upper()

            # Chama o controller para realizar o cadastro
            self.controller.cadastrar_motorista(
                cpf,
                nome,
                nascimento,
                oculos,
                placa,
                cor,
                marca_id,
                marca_nome,
                marca_sigla,
            )

            messagebox.showinfo("Sucesso", "Motorista cadastrado com sucesso!")
        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro de valor: {ve}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MotoristaApp(root)
    root.mainloop()
