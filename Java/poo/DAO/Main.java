package Java.poo.DAO;

public class Main {
    public static void main(String[] args) {
        try (PessoaDAO dao = new PessoaDAO("Alunos", "root", "root")) {
            // Instancias da classe
            Pessoa pessoa1 = new Pessoa(1, "Rafael", 39, (float) 1.88);
            Pessoa pessoa2 = new Pessoa(2, "Caroline", 30, (float) 1.7);
            Pessoa pessoa3 = new Pessoa(3, "Ikit Claw", 45, (float) 1.62);
            // Insere pessoa - C
            dao.inserirPessoa(pessoa1);
            dao.inserirPessoa(pessoa2);
            dao.inserirPessoa(pessoa3);
            // Exibe todas as pessoas
            System.out.println("Todas as pessoas:");
            dao.obterTodasPessoas().forEach(System.out::println);
            // Alterar uma pessoa - U
            dao.alterarPessoa(1, "Raphael", null, (float) 1.83);
            System.out.println("Pessoa após alteração:");
            System.out.println(dao.obterPessoaPorId(1));
            // Apagar uma pessoa - D
            dao.apagarPessoa(3);
            System.out.println("Pessoa após exclusão:");
            System.out.println(dao.obterPessoaPorId(3));
            // Apagar uma pessoa - D
            dao.apagarPessoa(3);
            pessoa2 = dao.obterPessoaPorId(3);
            System.out.println(pessoa2);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }

}
