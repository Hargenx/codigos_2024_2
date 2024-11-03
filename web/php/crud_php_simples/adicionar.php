<?php
require 'conexao.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = $_POST['nome'];
    $plataforma = $_POST['plataforma'];
    $genero = $_POST['genero'];
    $stmt = $pdo->prepare("INSERT INTO jogos (nome, plataforma, genero) VALUES (:nome, :plataforma, :genero)");
    $stmt->execute(['nome' => $nome, 'plataforma' => $plataforma, 'genero' => $genero]);
    header("Location: index.html");
}
