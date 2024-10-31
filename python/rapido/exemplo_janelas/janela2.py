
import tkinter as tk
import janela1

class Janela2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela 2")
        self.geometry("400x300")

        self.button = tk.Button(self, text="Abrir Janela1", command=self.open_janela1)
        self.button.pack(pady=20)

    def open_janela1(self):
        janela1 = Janela1()
        janela1.mainloop()

if __name__ == "__main__":
    janela2 = Janela2()
    janela2.mainloop()
