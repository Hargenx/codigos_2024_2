import os
import sys
import tkinter as tk
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 
import janela2

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("400x300")

        self.button = tk.Button(self, text="Abrir Janela2", command=self.open_janela2)
        self.button.pack(pady=20)

    def open_janela2(self):
        janela2 = janela2(self)
        janela2.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
