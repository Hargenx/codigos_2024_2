import tkinter as tk
import sys
import os
# Função para abrir a janela "Sobre"
def abrir_segunda_janela():
    # Encontra o caminho do arquivo sobre.py onde quer que ele esteja
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sobre_script = os.path.join(script_dir, 'sobre.py')
    
    # Executa o sobre.py usando o sistema
    os.system(f'{sys.executable} "{sobre_script}"')
def sair():
    janela.quit()
janela = tk.Tk()
janela.geometry('320x150') 
menubar = tk.Menu(janela)
janela.config(menu=menubar)
menu_arquivo = tk.Menu(menubar, tearoff=0)
menu_arquivo.add_command(label='Abrir')
menu_arquivo.add_command(label='Fechar')
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair', command=sair)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_ajuda = tk.Menu(menubar, tearoff=0)
menu_ajuda.add_command(label='Bem-vindo')
menu_ajuda.add_command(label='Sobre', command=abrir_segunda_janela)
menubar.add_cascade(label="Ajuda", menu=menu_ajuda)
janela.mainloop()





