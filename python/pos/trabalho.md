# Avaliação

**Disciplina**: Linguagem Python  
**Professor**: Raphael Mauricio Sanches de Jesus  
**Período**: Pós-Graduação  
**Data de Entrega**: 11/11/2024

---

## **Título do Trabalho**  

    **Desenvolvimento de uma Aplicação de Análise de Dados Integrada com Flask e Streamlit**

---

### **Objetivo**

O objetivo deste trabalho é aplicar os conceitos discutidos em aula, utilizando Python em diferentes paradigmas de programação, para desenvolver uma aplicação completa. O projeto deverá integrar os seguintes elementos:

1. **Orientação a Objetos**: Implementação de classes para organização do código.
2. **Paradigma Funcional**: Utilização de funções de alta ordem e expressões lambda.
3. **Computação Concorrente**: Implementação de uma API Flask e interface interativa com Streamlit em execução simultânea.
4. **Desenvolvimento Web**: Criação de uma API RESTful utilizando Flask.
5. **Ciência de Dados**: Manipulação e visualização de dados usando bibliotecas como Pandas e Matplotlib.

---

### **Descrição do Trabalho**

Você deverá desenvolver uma aplicação que atenda aos seguintes requisitos:

1. **Conjunto de Dados**:  
   - Utilize um conjunto de dados de sua escolha (recomendação: conjuntos de dados do Kaggle). O conjunto de dados deve ter, no mínimo, 500 registros e conter dados categóricos e numéricos.

2. **Classes e Organização do Código**:
   - Crie classes para:
     - Carregamento e pré-processamento dos dados.
     - Análises estatísticas e visualização.

3. **API Flask**:
   - Implemente uma API RESTful com os seguintes endpoints:
     - `GET /api/statistics`: Retorna estatísticas básicas dos dados (média, mediana, desvio padrão).
     - `GET /api/record/<id>`: Retorna informações detalhadas de um registro específico com base em seu ID.

4. **Interface Interativa com Streamlit**:
   - A interface deve permitir:
     - Upload de novos arquivos CSV.
     - Visualização de estatísticas e gráficos.
     - Consulta interativa aos endpoints da API.

5. **Visualização de Dados**:
   - Geração de gráficos como histogramas, gráficos de dispersão e gráficos de barras utilizando Matplotlib ou Seaborn.

6. **Programação Concorrente**:
   - A aplicação Flask e Streamlit devem rodar simultaneamente, permitindo que a interface consuma dados da API em tempo real.

---

### **Critérios de Avaliação**

1. **Funcionalidade e Correção do Código** (30 pontos):
   - O projeto deve ser funcional, atender aos requisitos propostos e não conter erros de execução.

2. **Organização e Orientação a Objetos** (20 pontos):
   - Boa utilização de classes e métodos, seguindo princípios de modularidade e reutilização de código.

3. **Integração com Flask e Streamlit** (20 pontos):
   - A API deve estar bem implementada e a interface Streamlit deve consumir os endpoints corretamente.

4. **Análise e Visualização de Dados** (20 pontos):
   - Estatísticas e gráficos devem ser relevantes e bem apresentados.

5. **Documentação e README.md** (10 pontos):
   - O projeto deve conter um `README.md` claro, explicando como configurar e executar a aplicação.

---

### **Entrega**

- Submeta o projeto no formato de um repositório Git (GitHub, GitLab ou similar). O repositório deve conter todos os arquivos necessários para execução, incluindo o `README.md` e o conjunto de dados utilizado.
- Instruções claras para configuração e execução devem ser incluídas no `README.md`.

---

### **Observações**

- Este é um trabalho grupo de até 3 integrantes. Dúvidas podem ser enviadas por e-mail ou discutidas durante o horário de aula.
- Trabalhos entregues fora do prazo sofrerão penalidades, conforme regulamento da disciplina.

---

**Boa sorte!**
