package Java.poo.abstrato;

public class Main {
    public static void main(String[] args) {
        Funcionario dev = new Desenvolvedor("Raphael", 12000, 1500);
        Funcionario gerente = new Gerente("Caroline", 10000, 2000);

        System.out.println("Salário do Desenvolvedor " + dev.getNome() + ": " + dev.calcularSalario());
        System.out.println("Salário do Gerente " + gerente.getNome() + ": " + gerente.calcularSalario());
    }
}
