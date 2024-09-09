#!/usr/bin/env python
''' shebang ou hashbang.
Ele é uma convenção em sistemas Unix-like, incluindo Linux e macOS, que indica ao
sistema operacional qual interpretador deve ser usado para executar o script.'''
from mrjob.job import MRJob

class ContaPalavras(MRJob):
    def mapper(self, _, linha):
        # Remove espaços em branco à direita e à esquerda e divide a linha em palavras
        palavras = linha.strip().lower().split()
        # Emite cada palavra com uma contagem inicial de 1
        for palavra in palavras:
            yield palavra, 1
    def reducer(self, palavra, contagem):
        # Soma as contagens para cada palavra
        yield palavra, sum(contagem)

if __name__ == '__main__':
    ContaPalavras.run()