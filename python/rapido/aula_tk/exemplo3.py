import tkinter as tk
def ao_focar(event):
    if entrada.get() == "Digite o seu nome aqui!":
        entrada.delete(0, "end")
        entrada.config(fg="black")  # Altera a cor do texto para preto
def ao_desfocar(event):
    if not entrada.get():
        entrada.insert(0, "Digite o seu nome aqui!")
        entrada.config(fg="gray")  # Altera a cor do texto de volta para cinza
janela = tk.Tk()
entrada = tk.Entry(width=40, bg="white", fg="gray")
entrada.pack()
entrada.insert(0, "Digite o seu nome aqui!")
# Quando a caixa de entrada ganha o foco, chame a função ao_focar
entrada.bind("<FocusIn>", ao_focar)
# Quando a caixa de entrada perde o foco, chame a função ao_desfocar
entrada.bind("<FocusOut>", ao_desfocar)
#Somnete para verificar o FocusOut
btn_botao = tk.Button(
    text = 'Ia',
)
btn_botao.pack()
janela.mainloop()
