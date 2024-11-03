<!DOCTYPE html>
<html>

<head>
    <title>Editar Jogo</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Editar Jogo</h1>
    <?php
    require 'conexao.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
        $id = $_GET['id'];
        $stmt = $pdo->prepare("SELECT * FROM jogos WHERE id = :id");
        $stmt->execute(['id' => $id]);
        $jogo = $stmt->fetch();
        if ($jogo) {
            echo '<form action="atualizar.php" method="post">';
            echo '<input type="hidden" name="id" value="' . $jogo['id'] . '">';
            echo '<label for="nome">Nome do Jogo:</label>';
            echo '<input type="text" name="nome" value="' . $jogo['nome'] . '" required><br>';
            echo '<label for="plataforma">Plataforma:</label>';
            echo '<input type="text" name="plataforma" value="' . $jogo['plataforma'] . '" required><br>';
            echo '<label for="genero">Gênero:</label>';
            echo '<input type="text" name="genero" value="' . $jogo['genero'] . '" required><br>';
            echo '<button type="submit">Atualizar</button>';
            echo '</form>';
        } else {
            echo '<p>Jogo não encontrado.</p>';
        }
    } else {
        echo '<p>Parâmetros inválidos.</p>';
    }
    echo '<a href="index.html">Retornar para Cadastro</a>';
    ?>
</body>

</html>