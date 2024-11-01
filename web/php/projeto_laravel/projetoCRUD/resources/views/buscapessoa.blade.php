<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Laravel 💘 PHP</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>

<body>
    <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
        <div class="card-header">Detalhes da pessoa</div>
        <div class="card-body">
            <h5 class="card-title">{{ $pessoa->nome }}</h5>
            <p class="card-text">id: {{ $pessoa->id }}<br />
                <br />
                email: {{ $pessoa->email }}<br />
                telefone: {{ $pessoa->telefone }}<br />
                endereco: {{ $pessoa->endereco }}<br />
                data_nascimento: {{ $pessoa->data_nascimento }}<br />
            </p>
        </div>
    </div>
    <a href="{{ route('listar') }}" class="btn btn-primary">Voltar</a>
</body>

</html>