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
    <h2>Listagem de Pessoas</h2>
    @if(session('success'))
    <div class="alert alert-success">
        {{ session('success') }}
    </div>
    @endif

    <table class="table table-striped table-bordered">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Telefone</th>
                <th>Endereço</th>
                <th>Data de Nascimento</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            @foreach($pessoas as $pessoa)
            <tr>
                <td>{{ $pessoa->id }}</td>
                <td>{{ $pessoa->nome }}</td>
                <td>{{ $pessoa->email }}</td>
                <td>{{ $pessoa->telefone }}</td>
                <td>{{ $pessoa->endereco }}</td>
                <td>{{ $pessoa->data_nascimento }}</td>
                <td>
                    <a href="{{ route('buscar', $pessoa->id) }}" class="btn btn-info">Detalhes</a>
                    <a href="{{ route('editar', $pessoa->id) }}" class="btn btn-outline-info">Alterar</a>
                    <a href="{{ route('confirmarExclusao', $pessoa->id) }}" class="btn btn-danger">Apagar</a>
                </td>
            </tr>
            @endforeach
        </tbody>
    </table>
    <br />
    <a href="{{ route('formulario') }}" class="btn btn-primary">Cadastrar</a>
</body>
</html>