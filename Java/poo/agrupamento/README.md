# Projeto de Agrupamento em Java

Este é um projeto desenvolvido para fins acadêmicos, voltado para alunos de graduação que desejam aprender e praticar conceitos de programação orientada a objetos (POO) em Java. O projeto inclui o uso de classes, enums, e diferentes estruturas de dados (`Set`, `List`, `Queue`, `Deque`) para simular o funcionamento de um restaurante.

## Objetivo

O objetivo deste projeto é demonstrar o uso de coleções em Java para agrupar e manipular dados, aplicando conceitos fundamentais de POO, como:

- **Classes e Objetos**: Estruturação de dados com classes `Pedido` e `Restaurante`.
- **Enums**: Uso de `enum` (`TipoPrato`) para representar tipos fixos de pratos.
- **Coleções Java**: Utilização de `Set`, `List`, `Queue`, e `Deque` para diferentes finalidades dentro do gerenciamento de pedidos em um restaurante.
- **Tratamento de Exceções**: Verificações e lançamentos de exceções para garantir a integridade dos dados.

## Estrutura do Projeto

O projeto contém as seguintes classes:

- **Pedido**: Representa um pedido no restaurante, com um número e um tipo de prato.
- **TipoPrato**: Enum que define os tipos de pratos disponíveis.
- **Restaurante**: Classe principal que simula o gerenciamento dos pedidos de um restaurante, utilizando diferentes tipos de coleções.

## Pré-requisitos

Para executar o projeto, é necessário ter:

- Java Development Kit (JDK) 8 ou superior.
- Um ambiente de desenvolvimento Java (IDE) como Eclipse, IntelliJ IDEA, ou VS Code com extensão Java.

## Como Executar

1. Clone o repositório ou faça o download do código fonte.
2. Importe o projeto em sua IDE de preferência.
3. Compile e execute a classe `Restaurante`.

```bash
javac Restaurante.java
java Restaurante
```

## Exemplo de Uso

A classe Restaurante adiciona alguns pedidos e exibe informações sobre os pratos únicos pedidos, a ordem dos pedidos, a fila de pedidos e as ações do chef.

## Saída Esperada

Ao executar o programa, a saída será similar a:

```java
    Pratos Únicos Pedidos: [PIZZA_4_QUIEJOS, HAMBURGUER_COM_BATATAS, SALADA_CAESAR]
    Ordem dos Pedidos: [Pedido #1: PIZZA_4_QUIEJOS, Pedido #2: HAMBURGUER_COM_BATATAS, Pedido #3: SALADA_CAESAR]
    Fila de Pedidos: [Pedido #3: SALADA_CAESAR]
    Ações do Chef: [Pedido #1: PIZZA_4_QUIEJOS, Pedido #2: HAMBURGUER_COM_BATATAS]
    Prato único: PIZZA_4_QUIEJOS
    Prato único: HAMBURGUER_COM_BATATAS
    Prato único: SALADA_CAESAR

```

## Contribuições

Este projeto é aberto para contribuições de alunos e desenvolvedores interessados em aprimorar suas habilidades em Java. Sinta-se à vontade para criar pull requests ou abrir issues para melhorias e correções.

## Licença

Este projeto é de uso acadêmico e educacional. Sinta-se livre para usar e modificar conforme necessário para fins educacionais.

_______
Nota: Este projeto foi criado como parte de uma atividade de ensino para alunos de graduação em cursos de Ciência da Computação, Engenharia de Software ou áreas afins.
