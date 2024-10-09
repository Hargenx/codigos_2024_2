import tkinter as tk

janela = tk.Tk()
ola = tk.Label(text="Oi, texto maior, bem grande para poder ter espaço...")
botao = tk.Button(
    text="Isso é fácil",
    width = 15,
    height = 15,
)

label = tk.Label(text="Nome")
entry = tk.Entry()

ola.pack()
entry.pack()
label.pack()
botao.pack()

entry.insert(0, "Raphael")

nome = entry.get()

print(nome)

janela.mainloop()
