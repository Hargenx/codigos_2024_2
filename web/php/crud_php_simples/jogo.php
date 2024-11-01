<?
class Jogo
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function adicionar($nome, $plataforma, $genero, $nota, $descricao)
    {
        $stmt = $this->pdo->prepare("INSERT INTO jogos (nome, plataforma, genero, nota, descricao) VALUES (?, ?, ?, ?, ?)");
        return $stmt->execute([$nome, $plataforma, $genero, $nota, $descricao]);
    }

    public function listar()
    {
        $stmt = $this->pdo->query("SELECT * FROM jogos");
        return $stmt->fetchAll();
    }

    public function editar($id, $nome, $plataforma, $genero, $nota, $descricao)
    {
        $stmt = $this->pdo->prepare("UPDATE jogos SET nome = ?, plataforma = ?, genero = ?, nota = ?, descricao = ? WHERE id = ?");
        return $stmt->execute([$nome, $plataforma, $genero, $nota, $descricao, $id]);
    }

    public function excluir($id)
    {
        $stmt = $this->pdo->prepare("DELETE FROM jogos WHERE id = ?");
        return $stmt->execute([$id]);
    }
}
