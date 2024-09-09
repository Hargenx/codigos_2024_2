#!/usr/bin/env python
''' shebang ou hashbang.
Ele é uma convenção em sistemas Unix-like, incluindo Linux e macOS, que indica ao
sistema operacional qual interpretador deve ser usado para executar o script.'''
import sys

palavra_atual = None
contagem_atual = 0
palavra = None
# Lê a entrada de sys.stdin
for linha in sys.stdin:
    # Remove espaços em branco à direita e à esquerda
    linha = linha.strip()
    # Faz o parsing da entrada
    palavra, contagem = linha.split('\t', 1)
    # Converte a contagem para int
    try:
        contagem = int(contagem)
    except ValueError:
        # Se a contagem não for um número, ignora esta linha
        continue
    ''' Esta parte assume que os dados estão ordenados pelo shuffle/sort,
     o que é o caso padrão'''
    if palavra_atual == palavra:
        contagem_atual += contagem
    else:
        if palavra_atual:
            # Emite a palavra anteriormente processada e sua contagem
            print(f'{palavra_atual}\t{contagem_atual}')
        contagem_atual = contagem
        palavra_atual = palavra
# Emite a última palavra se necessário
if palavra_atual == palavra:
    print('%s\t%s' % (palavra_atual, contagem_atual))