import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root, go_to_main_screen, go_to_register_screen):
        self.root = root
        self.go_to_main_screen = go_to_main_screen
        self.go_to_register_screen = go_to_register_screen
        self.root.title("Login")
        self.root.geometry("400x600")  # Definir tamanho da janela

        # Definir o fundo da janela
        self.root.configure(bg='#2c3e50')

        # Centralizar os widgets
        self.frame = tk.Frame(root, bg='#34495e')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Título
        self.label_title = tk.Label(self.frame, text="LOGIN", font=("Arial", 24, "bold"), bg='#34495e', fg='white')
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

        # Botão de login
        self.btn_login = tk.Button(self.frame, text="Entrar", font=("Arial", 14), command=self.login, bg='#1abc9c', fg='white', bd=0, width=10)
        self.btn_login.grid(row=3, column=0, columnspan=2, pady=20)

        # Botão de cadastro
        self.btn_register = tk.Button(self.frame, text="Cadastrar", font=("Arial", 14), command=self.go_to_register_screen, bg='#1abc9c', fg='white', bd=0, width=10)
        self.btn_register.grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        # Pegar o valor dos campos
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Exemplo de validação simples (substitua pela lógica real de validação com banco de dados)
        if username == "admin" and password == "123":
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.go_to_main_screen()  # Navegar para a tela principal
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

