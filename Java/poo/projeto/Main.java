package Java.poo.projeto;

import java.util.Date;

public class Main {
    public static void main(String[] args) {
        Pessoa aluno = new Aluno("Raphael", new Date(), "Av. Don helder, 0000", 123456789, "raphael.jesus@email.br", "123456789", 8.5f, "A");

        System.out.println(aluno.toString());

    }
}
