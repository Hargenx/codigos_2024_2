import tkinter as tk
from tkinter import ttk


class TreeviewExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Treeview")

        # Criar o Treeview
        self.tree = ttk.Treeview(
            root, columns=("Nome", "Idade", "Profissão"), show="headings"
        )

        # Definir os cabeçalhos das colunas
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Idade", text="Idade")
        self.tree.heading("Profissão", text="Profissão")

        # Definir a largura das colunas
        self.tree.column("Nome", width=150)
        self.tree.column("Idade", width=80)
        self.tree.column("Profissão", width=150)

        # Adicionar alguns dados
        self.tree.insert("", "end", values=("Raphael", 40, "Desenvolvedor"))
        self.tree.insert("", "end", values=("Caroline", 31, "Nutricionista"))
        self.tree.insert("", "end", values=("Sara", 68, "Professora"))

        # Mostrar o Treeview na tela
        self.tree.pack(pady=20)

        # Botão para adicionar mais uma linha de exemplo
        self.btn_add_row = tk.Button(
            root, text="Adicionar Linha", command=self.adicionar_linha
        )
        self.btn_add_row.pack(pady=10)

    def adicionar_linha(self):
        # Exemplo de como adicionar uma nova linha ao Treeview
        self.tree.insert("", "end", values=("Gilson", 68, "Contador"))


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeviewExampleApp(root)
    root.mainloop()
