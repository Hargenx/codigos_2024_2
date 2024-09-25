package com.examplo;

import java.sql.SQLException;
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;

public class PessoaDAO implements AutoCloseable {
    
    private final Connection conexao;

    public PessoaDAO(String nomeBanco) {
        try {
            // Define o caminho relativo ao diretório do projeto para o banco de dados
            Path currentRelativePath = Paths.get("");
            String projectPath = currentRelativePath.toAbsolutePath().toString();
            
            // Diretório onde o banco de dados será salvo dentro do projeto
            String dbDirectory = projectPath + File.separator + "db";
            File directory = new File(dbDirectory);
            
            // Verifica se o diretório existe, caso contrário cria
            if (!directory.exists()) {
                directory.mkdirs();
                System.out.println("Diretório criado: " + dbDirectory);
            }
            
            // Define a URL para o banco de dados SQLite
            String url = "jdbc:sqlite:" + dbDirectory + nomeBanco + ".db"; // Adiciona a extensão .db
            conexao = DriverManager.getConnection(url);
            criarTabelaPessoas();
        } catch (SQLException e) {
            System.err.println("Erro ao conectar ou criar o banco de dados: " + e.getMessage());
            throw new RuntimeException("Erro ao conectar ou criar o banco de dados", e);
        }
    }

    private void criarTabelaPessoas() {
        String sql = "CREATE TABLE IF NOT EXISTS pessoas ("
                + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                + "nome TEXT,"
                + "idade INTEGER,"
                + "altura REAL"
                + ")";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Erro ao criar tabela pessoas: " + e.getMessage());
            throw new RuntimeException("Erro ao criar tabela pessoas", e);
        }
    }
     

    public void inserirPessoa(Pessoa pessoa) {
        String sql = "INSERT INTO pessoas (id, nome, idade, altura) VALUES (?, ?, ?, ?)";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            statement.setInt(1, pessoa.getId());
            statement.setString(2, pessoa.getNome());
            statement.setInt(3, pessoa.getIdade());
            statement.setFloat(4, pessoa.getAltura());
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Erro ao inserir pessoa no banco de dados: " + e.getMessage());
            throw new RuntimeException("Erro ao inserir pessoa no banco de dados", e);
        }
    }

      

    public Pessoa obterPessoaPorId(int id) {
        String sql = "SELECT id, nome, idade, altura FROM pessoas WHERE id = ?";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            statement.setInt(1, id);
            try (ResultSet result = statement.executeQuery()) {
                if (!result.next()) {
                    return null;
                }
                return new Pessoa(result.getInt("id"),
                        result.getString("nome"),
                        result.getInt("idade"),
                        result.getFloat("altura"));
            }
        } catch (SQLException e) {
            System.err.println("Erro ao obter pessoa por ID: " + e.getMessage());
            throw new RuntimeException("Erro ao obter pessoa por ID", e);
        }
    }
      

    public List<Pessoa> obterTodasPessoas() {
        List<Pessoa> pessoas = new ArrayList<>();
        String sql = "SELECT id, nome, idade, altura FROM pessoas";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            try (ResultSet result = statement.executeQuery()) {
                while (result.next()) {
                    pessoas.add(new Pessoa(result.getInt("id"),
                            result.getString("nome"),
                            result.getInt("idade"),
                            result.getFloat("altura")));
                }
            }
        } catch (SQLException e) {
            System.err.println("Erro ao obter todas as pessoas: " + e.getMessage());
            throw new RuntimeException("Erro ao obter todas as pessoas", e);
        }
        return pessoas;
    }
      

    public void alterarPessoa(int id, String nome, Integer idade, Float altura) {
        // Inicializa o SQL
        StringBuilder sqlBuilder = new StringBuilder("UPDATE pessoas SET ");
        List<Object> parametros = new ArrayList<>();

        // Adiciona campos ao SQL apenas se os valores forem fornecidos (não nulos)
        if (nome != null) {
            sqlBuilder.append("nome = ?,");
            parametros.add(nome);
        }
        if (idade != null) {
            sqlBuilder.append("idade = ?,");
            parametros.add(idade);
        }
        if (altura != null) {
            sqlBuilder.append("altura = ?,");
            parametros.add(altura);
        }

        // Remove a vírgula extra no final, se houver
        if (parametros.isEmpty()) {
            throw new RuntimeException("Nenhum campo para atualizar foi fornecido.");
        }

        // Remove a última vírgula e adiciona a cláusula WHERE
        sqlBuilder.setLength(sqlBuilder.length() - 1); // Remove a vírgula final
        sqlBuilder.append(" WHERE id = ?");
        parametros.add(id);

        // Prepara a execução do SQL
        try (PreparedStatement statement = conexao.prepareStatement(sqlBuilder.toString())) {
            for (int i = 0; i < parametros.size(); i++) {
                statement.setObject(i + 1, parametros.get(i));
            }
            statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Erro ao alterar pessoa: " + e.getMessage());
            throw new RuntimeException("Erro ao alterar pessoa", e);
        }
    }
      
    public void hakai() {
        String sql = "DROP TABLE IF EXISTS pessoas";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Erro ao apagar tabela pessoas: " + e.getMessage());
            throw new RuntimeException("Erro ao apagar tabela pessoas", e);
        }
    }

    public void apagarPessoa(int id) {
        String sql = "DELETE FROM pessoas WHERE id = ?";
        try (PreparedStatement statement = conexao.prepareStatement(sql)) {
            statement.setInt(1, id);
            statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Erro ao apagar pessoa: " + e.getMessage());
            throw new RuntimeException("Erro ao apagar pessoa", e);
        }
    }
    
    @Override
    public void close() {
        try {
            if (conexao != null && !conexao.isClosed()) {
                conexao.close();
            }
        } catch (SQLException e) {
            System.err.println("Erro ao fechar conexão com o banco de dados: " + e.getMessage());
        }
    }
}
