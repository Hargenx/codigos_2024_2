import tkinter as tk
from tkinter import ttk
import sqlite3


# Função para criar o banco de dados e inserir dados
def criar_banco():
    conn = sqlite3.connect("motoristas.db")
    cursor = conn.cursor()

    # Criar tabela Motoristas se não existir
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Motoristas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        profissao TEXT NOT NULL
    )
    """
    )

    # Inserir alguns dados se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM Motoristas")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            """
        INSERT INTO Motoristas (nome, idade, profissao)
        VALUES (?, ?, ?)
        """,
            [
                ("Ana", 25, "Engenheira"),
                ("Carlos", 30, "Professor"),
                ("Beatriz", 28, "Médica"),
                ("João", 40, "Advogado"),
            ],
        )

    conn.commit()
    conn.close()


# Função para carregar dados do banco no Treeview
def carregar_dados(tree):
    conn = sqlite3.connect("motoristas.db")
    cursor = conn.cursor()

    # Selecionar todos os dados da tabela Motoristas
    cursor.execute("SELECT * FROM Motoristas")
    registros = cursor.fetchall()

    # Limpar o Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Inserir dados no Treeview
    for row in registros:
        tree.insert("", "end", values=row)

    conn.close()


# Classe da aplicação com o Treeview
class MotoristaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Motoristas")

        # Criar Treeview com colunas
        self.tree = ttk.Treeview(
            root, columns=("ID", "Nome", "Idade", "Profissão"), show="headings"
        )

        # Definir os cabeçalhos das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Idade", text="Idade")
        self.tree.heading("Profissão", text="Profissão")

        # Definir a largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=150)
        self.tree.column("Idade", width=80)
        self.tree.column("Profissão", width=150)

        # Mostrar o Treeview
        self.tree.pack(pady=20)

        # Botão para recarregar os dados do banco
        self.btn_carregar = tk.Button(
            root, text="Carregar Dados", command=lambda: carregar_dados(self.tree)
        )
        self.btn_carregar.pack(pady=10)

        # Carregar os dados automaticamente ao iniciar
        carregar_dados(self.tree)


if __name__ == "__main__":
    # Criar o banco de dados e inserir dados, se necessário
    criar_banco()

    # Iniciar a interface Tkinter
    root = tk.Tk()
    app = MotoristaApp(root)
    root.mainloop()
