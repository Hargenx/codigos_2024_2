#!/usr/bin/env python
''' shebang ou hashbang.
Ele é uma convenção em sistemas Unix-like, incluindo Linux e macOS, que indica ao
sistema operacional qual interpretador deve ser usado para executar o script.'''
import sys
import re

# Expressão regular para separar palavras
PALAVRA_RE = re.compile(r"[\w']+")
for linha in sys.stdin:
    # Remove espaços em branco à direita e à esquerda e divide a linha em palavras
    palavras = PALAVRA_RE.findall(linha.strip().lower())
    # Emite cada palavra com uma contagem inicial de 1
    for palavra in palavras:
        print(f'{palavra}\t{1}')