import tkinter as tk
import random

# Função para criar uma janela divertida
def janela_divertida():
    cores = ['red', 'blue', 'green', 'purple', 'orange', 'pink']
    segunda_janela = tk.Tk()
    segunda_janela.title('Sobre')
    segunda_janela.geometry('300x200')

    # Texto divertido
    texto = tk.Label(segunda_janela, text="Bem-vindo à janela Sobre!", font=("Comic Sans MS", 14))
    texto.pack(pady=20)

    # Mudança de cor divertida
    def mudar_cor():
        cor_aleatoria = random.choice(cores)
        segunda_janela.configure(bg=cor_aleatoria)

    botao_cor = tk.Button(segunda_janela, text="Mudar Cor", command=mudar_cor)
    botao_cor.pack(pady=10)

    segunda_janela.mainloop()

# Executa a janela divertida
if __name__ == "__main__":
    janela_divertida()
