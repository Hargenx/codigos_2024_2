<?php
$host = "localhost";
$username = "root";
$password = "";

try {
    $pdo = new PDO("mysql:host=$host;", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    // Cria o banco de dados
    $pdo->exec("CREATE DATABASE IF NOT EXISTS jogos_db");
    $pdo->exec("USE jogos_db");
    // Cria a tabela de jogos
    $pdo->exec("CREATE TABLE IF NOT EXISTS jogos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        plataforma VARCHAR(255) NOT NULL,
        genero VARCHAR(255) NOT NULL
        )");
} catch (PDOException $e) {
    die("Erro na conexão com o banco de dados: " . $e->getMessage());
}
