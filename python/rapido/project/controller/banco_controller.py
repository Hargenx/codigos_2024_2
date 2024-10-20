import sqlite3
from model.dono import Dono
from model.marca import Marca
from model.pessoa import Pessoa
from model.veiculo import Veiculo
import os


class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            self.criar_tabelas()  # Certifica-se de que as tabelas são criadas ao conectar
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabelas(self):
        self.criar_tabela_pessoa()
        self.criar_tabela_dono()
        self.criar_tabela_marca()
        self.criar_tabela_veiculo()

    def criar_tabela_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa (
                                cpf INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                nascimento DATE,
                                oculos BOOLEAN
                                )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Pessoa: {e}")

    def criar_tabela_dono(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Dono (
                        email TEXT PRIMARY KEY,
                        nome TEXT,
                        senha TEXT NOT NULL
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Dono: {e}")

    def criar_tabela_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                sigla TEXT
                                )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Marca: {e}")

    def criar_tabela_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo (
                placa TEXT PRIMARY KEY,
                cor TEXT NOT NULL,
                cpf_proprietario INTEGER,
                id_marca INTEGER,
                FOREIGN KEY(cpf_proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(id_marca) REFERENCES Marca(id))"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Veiculo: {e}")

    def inserir_pessoa(self, pessoa: Pessoa):
        """Função para inserir uma pessoa no banco de dados."""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)",
                    (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir pessoa: {e}")

    def inserir_veiculo(self, veiculo: Veiculo):
        """Função para inserir um veículo no banco de dados."""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Veiculo (placa, cor, cpf_proprietario, id_marca) VALUES (?, ?, ?, ?)",
                    (
                        veiculo.placa,
                        veiculo.cor,
                        veiculo.cpf_proprietario,
                        veiculo.id_marca,
                    ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir veículo: {e}")

    def inserir_dono(self, dono: Dono):
        """Função para inserir um dono no banco de dados."""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Dono (email, nome, senha) VALUES (?, ?, ?)",
                    (dono.email, dono.nome, dono.senha),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir dono: {e}")

    def buscar_dono_por_email(self, email: str):
        """Função para buscar um dono pelo email."""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Dono WHERE email=?", (email,))
                row = cursor.fetchone()
                if row:
                    return Dono(email=row[0], nome=row[1], senha=row[2])
            except sqlite3.Error as e:
                print(f"Erro ao buscar dono por email: {e}")
        return None

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
