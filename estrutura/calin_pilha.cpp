#include <iostream>
#include<stdio.h>
#include<stdlib.h>

#define TAM 100

typedef struct{
    int topo;
    int bin[TAM];
}pilhavet;

void empilhar(int resto, pilhavet *p){
    if(p -> topo == TAM - 1){
        printf("Pilha cheia");
        exit(1);
    }
        p -> topo++;
        p -> bin[p -> topo] = resto;
}

int desempilha(pilhavet *p){
    int n;
    if(p -> topo < 0){
        printf("Pilha vazia");
        exit(1);
    }
        n = p -> bin[p -> topo];
        p -> topo--;
        return n;
}

int main(){
    pilhavet pilha;
    int resto;
    int num;
    pilha.topo = -1;
    std::cout << "Digite o valor para ser convertido para binário: ";
    std::cin >> num;
    while(num > 0){
        resto = num % 2;
        empilhar(resto, &pilha);
        num = num / 2;
    }
    while(pilha.topo >= 0){
        std::cout << desempilha(&pilha);
    }
    return 0;
}