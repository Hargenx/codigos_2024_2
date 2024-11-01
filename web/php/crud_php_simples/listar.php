<!DOCTYPE html>
<html>

<head>
    <title>Lista de Jogos</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Lista de Jogos</h1>
    <ul>
        <?php
        require 'conexao.php';
        $stmt = $pdo->query("SELECT * FROM jogos");
        while ($row = $stmt->fetch()) {
            echo "<li>{$row['nome']} (Plataforma: {$row['plataforma']}, Gênero: {$row['genero']})</li>";
            echo "<a href='editar.php?id={$row['id']}'>Editar</a> ";
            echo "<a href='excluir.php?id={$row['id']}'>Excluir</a></li>";
        }
        ?>
        <br><a href="index.html">Voltar</a>
    </ul>
</body>

</html>