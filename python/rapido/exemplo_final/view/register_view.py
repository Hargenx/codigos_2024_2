import tkinter as tk
from tkinter import messagebox

class RegisterApp:
    def __init__(self, root, go_to_login_screen):
        self.root = root
        self.go_to_login_screen = go_to_login_screen
        self.root.title("Cadastro de Usuário")
        self.root.geometry("400x600")

        # Definir o fundo da janela
        self.root.configure(bg='#2c3e50')

        # Centralizar os widgets
        self.frame = tk.Frame(root, bg='#34495e')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Título
        self.label_title = tk.Label(self.frame, text="CADASTRO", font=("Arial", 24, "bold"), bg='#34495e', fg='white')
        self.label_title.grid(row=0, column=0, columnspan=2, pady=20)

        # Login (Usuário)
        self.label_username = tk.Label(self.frame, text="Usuário", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_username.grid(row=1, column=0, padx=10, pady=10)
        self.entry_username = tk.Entry(self.frame, font=("Arial", 14))
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)

        # Senha
        self.label_password = tk.Label(self.frame, text="Senha", font=("Arial", 14), bg='#34495e', fg='white')
        self.label_password.grid(row=2, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(self.frame, font=("Arial", 14), show='*')
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        # Botão de cadastrar
        self.btn_register = tk.Button(self.frame, text="Cadastrar", font=("Arial", 14), command=self.register, bg='#1abc9c', fg='white', bd=0, width=10)
        self.btn_register.grid(row=3, column=0, columnspan=2, pady=20)

        # Botão de voltar ao login
        self.btn_back = tk.Button(self.frame, text="Voltar", font=("Arial", 14), command=self.go_to_login_screen, bg='#1abc9c', fg='white', bd=0, width=10)
        self.btn_back.grid(row=4, column=0, columnspan=2, pady=10)

    def register(self):
        # Lógica de cadastro de usuário (exemplo simples)
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validação simples para exemplo
        if username and password:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.go_to_login_screen()  # Voltar para a tela de login após o cadastro
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

