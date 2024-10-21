# Projeto de Visualização de Dados de Importação e Exportação

Este é um exemplo de projeto desenvolvido para as turmas de graduação, com o objetivo de demonstrar como utilizar ferramentas modernas de visualização de dados em **Python**. A aplicação faz uso de **Streamlit**, **Plotly** e **Pandas** para criar uma interface interativa que permite a exploração de um conjunto de dados de importação e exportação.

Dataset utilizado: <https://www.kaggle.com/datasets/willianoliveiragibin/imports-exports-v23>

## Objetivos

- Demonstrar o uso de bibliotecas de visualização e análise de dados em Python.
- Prover uma interface gráfica interativa que permita a visualização e análise de dados filtrados.
- Mostrar a importância da organização de código e documentação em projetos de visualização de dados.

## Ferramentas Utilizadas

- **Python**: Linguagem de programação utilizada para manipulação de dados e lógica da aplicação.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Biblioteca para criar gráficos interativos.
- **Streamlit**: Framework para criar aplicativos web interativos de forma rápida e simples.

## Funcionalidades

- **Filtragem de dados por país**: Os usuários podem selecionar um país específico através de uma caixa de seleção.
- **Filtragem por tipo de transação**: Usando botões de rádio, o usuário pode escolher entre transações de importação ou exportação.
- **Filtragem por categoria**: Permite selecionar uma ou mais categorias de produtos.
- **Visualizações interativas**:
  - Gráficos de barras para visualizar a quantidade total de transações por categoria.
  - Gráficos de pizza para visualizar o valor total por categoria.
  - Gráficos de linha para mostrar a evolução do peso total ao longo do tempo.
  
## Como Executar o Projeto

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/professorRaphael/exemplo-streamlit.git
    ```

2. Certifique-se de ter o Python instalado. Instale as dependências necessárias:

    ```bash
    pip install streamlit pandas plotly
    ```

3. Execute a aplicação utilizando o Streamlit:

    ```bash
    streamlit run main.py
    ```

## Estrutura do projeto

```bash
projeto_visualizacao
│
├── Imports_Exports_Dataset new.csv  # Arquivo de dados CSV utilizado no projeto
├── app.py                           # Script principal com a aplicação Streamlit
└── README.md                        # Arquivo de documentação do projeto
```

## Exemplo de Uso

Esta aplicação foi desenvolvida com fins educacionais, para turmas de graduação. Ela pode ser utilizada em disciplinas de ciência de dados, visualização de dados ou programação, para ilustrar como criar dashboards interativos e trabalhar com dados do mundo real.

## Contribuições

Se você deseja contribuir com melhorias ou ajustes, sinta-se à vontade para abrir issues ou enviar pull requests.

____

Autor: Raphael M. S. de Jesus
