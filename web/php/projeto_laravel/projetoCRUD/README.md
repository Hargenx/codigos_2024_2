# Projeto CRUD de Pessoas com Laravel

Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) desenvolvida em Laravel, permitindo o gerenciamento de informações de pessoas. A aplicação permite cadastrar, visualizar, atualizar e excluir registros de pessoas no banco de dados.

## Funcionalidades

- **Listar Pessoas**: Exibe uma tabela com todas as pessoas cadastradas.
- **Cadastrar Pessoa**: Formulário para cadastrar uma nova pessoa com os campos de nome, e-mail, telefone, endereço e data de nascimento.
- **Editar Pessoa**: Permite atualizar as informações de uma pessoa existente.
- **Excluir Pessoa**: Opção de exclusão de um registro de pessoa, com uma página de confirmação antes de excluir.

## Estrutura do Banco de Dados

A tabela `pessoas` possui os seguintes campos:

- `id`: Identificador único da pessoa (chave primária).
- `nome`: Nome da pessoa (string com até 50 caracteres).
- `email`: Endereço de e-mail da pessoa (string).
- `telefone`: Número de telefone da pessoa (string).
- `endereco`: Endereço da pessoa (string).
- `data_nascimento`: Data de nascimento da pessoa (formato de data).
- `created_at` e `updated_at`: Timestamps para criação e atualização dos registros.

## Pré-requisitos

- PHP >= 8.0
- Composer
- MySQL ou outro banco de dados compatível com Laravel
- Node.js e NPM (opcional, para instalação de pacotes frontend)

## Configuração do Projeto

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências do projeto:

    ```bash
    composer install
    ```

3. Configure o arquivo `.env` com as informações do banco de dados:

    ```dotenv
    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=nome_do_banco
    DB_USERNAME=usuario
    DB_PASSWORD=senha
    ```

4. Gere a chave de aplicativo do Laravel:

    ```bash
    php artisan key:generate
    ```

5. Execute as migrações para criar a tabela `pessoas`:

    ```bash
    php artisan migrate
    ```

## Executando o Projeto

Para iniciar o servidor de desenvolvimento do Laravel, execute o comando:

```bash
php artisan serve
```

A aplicação estará disponível em <http://localhost:8000>.

## Estrutura de Arquivos

- app/Http/Controllers/PessoaController.php: Controlador principal que gerencia as operações de CRUD.
- database/migrations/: Contém as migrações para a criação da tabela pessoas.
- resources/views/: Contém as views Blade para listar, cadastrar, editar e excluir pessoas.
- routes/web.php: Define as rotas da aplicação para acessar as funcionalidades de CRUD.

## Uso da Aplicação

- Acesse a página principal em <http://localhost:8000> para visualizar a lista de pessoas.
- Clique em "Cadastrar" para adicionar uma nova pessoa.
- Use o botão "Alterar" para editar as informações de uma pessoa.
- Clique em "Apagar" para acessar a página de confirmação de exclusão e confirmar ou cancelar a exclusão.

## Observações

Este projeto é um exemplo simples de CRUD em Laravel e pode ser expandido para incluir funcionalidades adicionais, como autenticação, paginação e pesquisa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é de uso livre e está sob a licença MIT.

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p>

<p align="center">
<a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

You may also try the [Laravel Bootcamp](https://bootcamp.laravel.com), where you will be guided through building a modern Laravel application from scratch.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains over 2000 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[Many](https://www.many.co.uk)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- **[DevSquad](https://devsquad.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[OP.GG](https://op.gg)**
- **[WebReinvent](https://webreinvent.com/?utm_source=laravel&utm_medium=github&utm_campaign=patreon-sponsors)**
- **[Lendio](https://lendio.com)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
