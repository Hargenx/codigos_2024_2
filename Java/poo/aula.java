package Java.poo;

import java.util.Scanner;
public class aula {

    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Digite o nome: ");
            pessoa.setNome(scan.nextLine());
            System.out.print("Digite a idade: ");
            int idade;
            idade = scan.nextInt();
            pessoa.setIdade(idade);
        }

        //pessoa.setIdade(40);
        /*pessoa.setNome("Raphael");*/
        
        System.out.println("Nome: " + pessoa.getNome() + ", Idade: " + pessoa.getIdade());
    }
}