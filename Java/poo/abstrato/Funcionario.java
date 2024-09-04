package Java.poo.abstrato;

public abstract class Funcionario implements Pagamento {
    private String nome;
    private double salarioBase;

    public Funcionario(String nome, double salarioBase) {
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    public String getNome() {
        return nome;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    // Método abstrato para calcular o salário, implementado pelas subclasses.
    public abstract double calcularSalario();
}
