import tkinter as tk
from tkinter import messagebox
from controller.motorista_controller import MotoristaController


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")
        self.controller = MotoristaController()

        # Botões para cadastrar motorista e veículo
        self.btn_cadastrar_motorista = tk.Button(
            root, text="Cadastrar Motorista", command=self.cadastrar_motorista
        )
        self.btn_cadastrar_motorista.grid(row=0, column=0)

        self.btn_cadastrar_veiculo = tk.Button(
            root, text="Cadastrar Veículo", command=self.cadastrar_veiculo
        )
        self.btn_cadastrar_veiculo.grid(row=0, column=1)

        # Listar veículos cadastrados
        self.label_veiculos = tk.Label(root, text="Veículos Cadastrados:")
        self.label_veiculos.grid(row=1, column=0, columnspan=2)

        self.listbox_veiculos = tk.Listbox(root, width=50)
        self.listbox_veiculos.grid(row=2, column=0, columnspan=2)
        self.atualizar_lista_veiculos()

    def cadastrar_motorista(self):
        # Aqui você redirecionaria para a tela de cadastro de motorista
        messagebox.showinfo(
            "Cadastrar", "Redirecionar para tela de cadastro de motorista"
        )

    def cadastrar_veiculo(self):
        # Aqui você redirecionaria para a tela de cadastro de veículo
        messagebox.showinfo(
            "Cadastrar", "Redirecionar para tela de cadastro de veículo"
        )

    def atualizar_lista_veiculos(self):
        # Obtenha os veículos do banco de dados
        veiculos = self.controller.banco.buscar_todos_veiculos()
        self.listbox_veiculos.delete(0, tk.END)
        for veiculo in veiculos:
            motorista = (
                veiculo.proprietario.nome if veiculo.proprietario else "Sem Motorista"
            )
            self.listbox_veiculos.insert(
                tk.END, f"{veiculo.placa} - {veiculo.marca.nome} ({motorista})"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
