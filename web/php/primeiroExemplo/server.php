<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email = $_POST["email"];

    $resposta = [
        'mensagem' => 'Dados registrados com sucesso',
        'dados' => [
            'nome' => $nome,
            'email' => $email
        ]
    ];

    header('Content-Type: application/json');
    echo json_encode($resposta);
}
