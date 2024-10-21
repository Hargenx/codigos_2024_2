import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Configura o caminho para o banco de dados SQLite
db_file = os.path.join(os.path.dirname(__file__), "usuarios.db")


# Função para conectar ao banco de dados e criar a tabela de usuários, se não existir
def conectar_banco():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    return conn


# Função para adicionar um usuário ao banco de dados
def adicionar_usuario(nome, email):
    conn = conectar_banco()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Email já cadastrado!")
    conn.close()


# Função para exibir os usuários armazenados no banco de dados
def exibir_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    rows = cursor.fetchall()
    conn.close()

    # Apaga o conteúdo da janela de exibição
    listbox.delete(0, tk.END)

    # Adiciona os usuários ao Listbox
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]} | Nome: {row[1]} | Email: {row[2]}")


# Função chamada ao clicar no botão de adicionar
def adicionar_callback():
    nome = entry_nome.get()
    email = entry_email.get()
    if not nome or not email:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return
    adicionar_usuario(nome, email)
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    exibir_usuarios()


# Criação da interface principal com Tkinter
app = tk.Tk()
app.title("Exemplo Simples com Tkinter e SQLite")
app.geometry("400x400")

# Rótulo e campo de texto para o nome
tk.Label(app, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(app, width=30)
entry_nome.pack(pady=5)

# Rótulo e campo de texto para o email
tk.Label(app, text="Email:").pack(pady=5)
entry_email = tk.Entry(app, width=30)
entry_email.pack(pady=5)

# Botão para adicionar usuário
btn_add = tk.Button(app, text="Adicionar Usuário", command=adicionar_callback)
btn_add.pack(pady=10)

# Listbox para exibir os usuários cadastrados
listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=20)

# Exibe os usuários ao iniciar a aplicação
exibir_usuarios()

# Executa o loop principal da aplicação
app.mainloop()
