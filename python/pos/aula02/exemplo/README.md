# Flask e Streamlit - Projeto de Exemplo Acadêmico

Este projeto é um **exemplo acadêmico** desenvolvido para demonstrar conceitos fundamentais de Python, como:
    - Programação Orientada a Objetos (OOP)
    - Paradigma Funcional
    - Computação Concorrente
    - Desenvolvimento Web com Flask
    - Visualização de Dados e Interfaces Interativas com Streamlit
    - Ciência de Dados usando Pandas e Matplotlib

## Objetivo

O projeto foi criado com fins **didáticos** para auxiliar no aprendizado dos temas discutidos nas aulas de Pós-Graduação, combinando ferramentas modernas e paradigmas de programação.

## Estrutura do Projeto

```console

├── app/
│   ├── data_loader.py         # Classe para carregar e pré-processar os dados
│   ├── analysis.py            # Classe para realizar análises nos dados
│   ├── api.py                 # API Flask para fornecer endpoints
├── streamlit_app.py           # Interface do Streamlit para interação com os dados
└── titanic.csv                # Conjunto de dados do Titanic (baixado do Kaggle)

```

### Arquivos principais

- **`data_loader.py`**: Responsável por carregar e pré-processar os dados.
- **`analysis.py`**: Contém métodos para análises de dados e visualizações.
- **`api.py`**: Cria uma API utilizando Flask para expor análises e dados.
- **`streamlit_app.py`**: Interface interativa criada com Streamlit para exploração de dados e visualizações.

## Pré-requisitos

Certifique-se de ter instalado:

- **Python 3.8+**
- **Pandas**
- **Matplotlib**
- **Flask**
- **Streamlit**

### Instalação

- Clone este repositório:

```bash
  git clone https://github.com/usuario/projeto-exemplo-academico.git
```

- Instale os pacotes necessários:

```bash
    pip install -r requirements.txt
```

- Baixe o conjunto de dados Titanic do Kaggle e salve-o como `titanic.csv` no diretório raiz.

## Como Executar

### Passo 1: API Flask

Execute a API Flask:

```bash
python app/api.py
```

A API estará disponível em `http://127.0.0.1:5000`.

### Passo 2: Streamlit

Abra outro terminal e execute o Streamlit:

```bash
streamlit run streamlit_app.py
```

A interface estará disponível no navegador, geralmente em `http://localhost:8501`.

## Funcionalidades

- **Visualização de Dados**: Veja os dados do Titanic carregados.
- **Análises Estatísticas**: Taxa de sobrevivência e distribuição de idades.
- **API REST**: Endpoints para acessar taxa de sobrevivência e informações de passageiros.
- **Interface Gráfica**: Utilize Streamlit para explorar os dados interativamente.

### Endpoints da API

- `GET /api/survival_rate`: Retorna a taxa de sobrevivência.
- `GET /api/passenger/<id>`: Retorna os dados do passageiro com o ID especificado.

## Aviso Legal

Este projeto é **exclusivamente para fins acadêmicos** e não deve ser utilizado em ambientes de produção. É uma aplicação simplificada para demonstrar conceitos e práticas de desenvolvimento em Python.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

-------

### Instruções Extras

Você pode personalizar o texto conforme necessário, adicionando mais detalhes sobre o uso ou modificações do projeto.
