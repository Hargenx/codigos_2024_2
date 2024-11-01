<!DOCTYPE html>
<html>

<head>
    <title>Excluir Jogo</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <h1>Excluir Jogo</h1>
    <?php
    require 'conexao.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id']) && isset($_GET['confirm']) && $_GET['confirm'] === 'true') {
        // Se confirmado, exclua o jogo aqui
        $id = $_GET['id'];
        $stmt = $pdo->prepare("DELETE FROM jogos WHERE id = :id");
        $stmt->execute(['id' => $id]);
        echo '<p>Jogo excluído com sucesso.</p>';
        echo '<a href="listar.php">Retornar para lista</a>';
    } elseif ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id'])) {
        $id = $_GET['id'];
        $stmt = $pdo->prepare("SELECT * FROM jogos WHERE id = :id");
        $stmt->execute(['id' => $id]);
        $jogo = $stmt->fetch();
        if ($jogo) {
            echo '<p>Tem certeza de que deseja excluir o jogo "' . $jogo['nome'] . '"?</p>';
            echo '<a href="excluir.php?id=' . $jogo['id'] . '&confirm=true">Sim</a>';
            echo '<a href="listar.php" class="excluir">Não</a>';
        } else {
            echo '<p>Jogo não encontrado.</p>';
        }
    } else {
        echo '<p>Parâmetros inválidos.</p>';
    }
    ?>
</body>

</html>