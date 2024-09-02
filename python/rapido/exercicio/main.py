class Contato:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} {self.sobrenome}, Email: {self.email}, Telefone: {self.telefone}"

class ControleContatos:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.contatos = self._carregar_contatos()

    def _carregar_contatos(self):
        """Carrega os contatos do arquivo para o dicionário."""
        contatos = {}
        try:
            with open(self.arquivo, 'r') as f:
                for linha in f:
                    nome, sobrenome, email, telefone = linha.strip().split(',')
                    contatos[email] = Contato(nome, sobrenome, email, telefone)
        except FileNotFoundError:
            pass
        return contatos

    def _salvar_contatos(self):
        """Salva os contatos do dicionário no arquivo."""
        with open(self.arquivo, 'w') as f:
            for contato in self.contatos.values():
                f.write(f"{contato.nome},{contato.sobrenome},{contato.email},{contato.telefone}\n")

    def adicionar_contato(self, contato):
        """Adiciona um novo contato ao dicionário e salva no arquivo."""
        self.contatos[contato.email] = contato
        self._salvar_contatos()

    def buscar_contato(self, email):
        """Busca um contato pelo email."""
        return self.contatos.get(email, "Contato não encontrado.")

    def remover_contato(self, email):
        """Remove um contato pelo email e atualiza o arquivo."""
        if email in self.contatos:
            del self.contatos[email]
            self._salvar_contatos()
        else:
            return "Contato não encontrado."

# Exemplo de uso
agenda = ControleContatos('contatos.txt')

# Adicionando um novo contato
novo_contato = Contato('Raphael', 'Jesus', 'raphael.jsus@estacio.br', '123456789')
agenda.adicionar_contato(novo_contato)

# Buscando um contato
print(agenda.buscar_contato("raphael.jsus@estacio.br"))

# Removendo um contato
#agenda.remover_contato("raphael.jsus@estacio.br")
print(agenda.buscar_contato("raphael.jsus@estacio.br"))
