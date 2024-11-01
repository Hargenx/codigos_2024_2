<?php
require 'conexao.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id'];
    $nome = $_POST['nome'];
    $plataforma = $_POST['plataforma'];
    $genero = $_POST['genero'];

    $stmt = $pdo->prepare("UPDATE jogos SET nome = :nome, plataforma = :plataforma, genero = :genero WHERE id = :id");
    $stmt->execute(['nome' => $nome, 'plataforma' => $plataforma, 'genero' => $genero, 'id' => $id]);

    header("Location: index.html"); // Redireciona para a página principal após a atualização
}
