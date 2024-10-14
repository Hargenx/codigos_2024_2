import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root, go_to_main_screen, go_to_register_screen):
        self.root = root
        self.go_to_main_screen = go_to_main_screen
        self.go_to_register_screen = go_to_register_screen
        self.root.title("Login")

        # Componentes da tela de login
        self.label_username = tk.Label(root, text="Login:")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(root, text="Senha:")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1)

        # Botões de ação
        self.btn_login = tk.Button(root, text="Entrar", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2)

        self.btn_register = tk.Button(
            root, text="Cadastrar", command=self.go_to_register_screen
        )
        self.btn_register.grid(row=3, column=0, columnspan=2)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Exemplo simples de validação (isso deve ser substituído por uma lógica de validação real)
        if username == "admin" and password == "123":
            self.go_to_main_screen()
        else:
            messagebox.showerror("Erro", "Login ou senha inválidos")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root, None, None)
    root.mainloop()
