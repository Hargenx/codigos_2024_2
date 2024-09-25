import sqlite3
import datetime
import os

# data = datetime.date.today() - Retorna a data do sistema em formato americano(2024-09-23)
dataSistema = datetime.date.today()
data = dataSistema.strftime('%d/%m/%Y')
nome_banco = os.path.join(os.path.dirname(__file__), 'cliente.db')
conn = sqlite3.connect(nome_banco)
def banco():
    cursor = conn.cursor()
    # criando a tabela
    try:
        cursor.execute(''' CREATE TABLE IF NOT EXISTS cliente(
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                idade INTEGER,
                                cpf VARCHAR(11) NOT NULL,
                                email TEXT,
                                telefone TEXT,
                                cidade TEXT,
                                uf VARCHAR(2),
                                criado_em DATE NOT NULL
                        ); ''')
    except sqlite3.Error as e:
        print('ERRO: Falha na criação do banco.', e)

# Inserindo os dados
def incluir(lista):
    try:
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO cliente (nome, idade, cpf, email, telefone, cidade, uf, criado_em) VALUES (?,?,?,?,?,?,?,?)', lista)
        conn.commit()
        print('Dados inseridos com sucesso.')
    except sqlite3.Error as e:
        print('ERRO: Falha na inserção dos dados.', e)

# Exibir os dados na tabela
def exibir():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cliente')
        for linha in cursor.fetchall():
            print(linha)
    except sqlite3.Error as e:
        print('ERRO: Falha na consulta dos dados.', e)

def dados():
    try:
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        cpf = int(input('Digite o CPF: '))
        email = str(input('Digite o email: '))
        telefone = str(input('Digite o telefone: '))
        cidade = str(input('Digite a cidade: '))
        uf = str(input('Digite o UF: '))
        lista = [(nome, idade, cpf, email, telefone, cidade, uf, data)]
        return lista
    except sqlite3.Error as e: # caso ocorra um erro na inserção dos dados
        print('ERRO: Falha na inserção dos dados.', e)

def leia_numero(numero):
    while True:
        try:
            num = int(input(numero))
        except (ValueError, TypeError):
            print('\n\033[031mERRO: Digite um numero inteiro válido!\033[m')
        except (KeyboardInterrupt) as ki:
            print('\n\033[031mERRO: Digite um numero inteiro válido!\033[m')
            print(f'\n\033[031mERRO: {ki}\033[m')
            return 0
        else:
            return num

def construir_menu(texto):
    print('_'*50)
    print(texto.center(50))
    print('_'*50)

def menu(opcoes):
    construir_menu('ESCOLA PASSEI')
    op = 1
    for item in opcoes:
        print(f'\033[32m{op}\033[34m - {item} \033[34m')
        op += 1
    print('_'*50)
    escolha = leia_numero('Digite a opção desejada: ')
    return escolha

def menu_principal():
    while True:
        opcao = menu(['Ler', 'Cadastrar', 'Sair'])
        match opcao:
            case 1:
                exibir()
            case 2:
                lista = dados()
                incluir(lista)
            case 3:
                print('Até mais ver! ^_^')
                break
            case _:
                print('\033[31mOpção invalida!!!\033[m')
if __name__ == '__main__':
    banco()
    menu_principal()
