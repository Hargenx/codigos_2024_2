import tkinter as tk
from view.login_view import LoginApp
from view.register_view import RegisterApp
from view.main_view import MainApp
from model.banco import BancoDeDados  # Certifique-se de ajustar o caminho

class Application:
    def __init__(self, root):
        self.root = root
        self.banco = BancoDeDados()  # Inicializando o banco de dados
        self.banco.conectar()  # Conectando ao banco de dados

        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        self.login_screen = LoginApp(self.root, self.show_main_screen, self.show_register_screen)

    def show_register_screen(self):
        self.clear_screen()
        self.register_screen = RegisterApp(self.root, self.show_login_screen)

    def show_main_screen(self):
        self.clear_screen()
        self.main_screen = MainApp(self.root, self.banco)  # Passando o banco de dados para MainApp

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
