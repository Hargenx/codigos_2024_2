import tkinter as tk
from tkinter import messagebox


class RegisterApp:
    def __init__(self, root, go_to_login_screen):
        self.root = root
        self.go_to_login_screen = go_to_login_screen
        self.root.title("Cadastro de Usuário")

        # Componentes da tela de cadastro
        self.label_username = tk.Label(root, text="Login:")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(root, text="Senha:")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1)

        # Botões de ação
        self.btn_register = tk.Button(root, text="Cadastrar", command=self.register)
        self.btn_register.grid(row=2, column=0, columnspan=2)

        self.btn_back_to_login = tk.Button(
            root, text="Voltar", command=self.go_to_login_screen
        )
        self.btn_back_to_login.grid(row=3, column=0, columnspan=2)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Exemplo simples de cadastro (deve ser substituído por uma lógica de persistência real)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.go_to_login_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterApp(root, None)
    root.mainloop()
