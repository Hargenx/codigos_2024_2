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
    <form method="post" action="{{ route('salvarPessoa') }}">
        @csrf
        <div class="form-group">
            <label for="nome">Nome</label>
            <input type="text" class="form-control" id="nome" name="nome" placeholder="Nome" value="{{old('nome')}}">
            @if ($errors->has('nome'))
            <div class="alert alert-danger">
                {{ $errors->first('nome') }}
            </div>
            @endif
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="Email">
            <label for="telefone">Telefone</label>
            <input type="text" class="form-control" id="telefone" name="telefone" placeholder="Telefone">
            <label for="endereco">Endereço</label>
            <input type="text" class="form-control" id="endereco" name="endereco" placeholder="Endereço">
            <label for="data_nascimento">Data Nascimento</label>
            <input type="date" class="form-control" id="data_nascimento" name="data_nascimento" placeholder="Data Nascimento">
        </div>
        <button type="submit" class="btn btn-primary">Cadastrar</button>
    </form>
    <br />
    <a href="{{ route('listar') }}" class="btn btn-primary">Voltar</a>
</body>

</html>