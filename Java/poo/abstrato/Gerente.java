package Java.poo.abstrato;

public class Gerente extends Funcionario {
    private double comissao;

    public Gerente(String nome, double salarioBase, double comissao) {
        super(nome, salarioBase);
        this.comissao = comissao;
    }

    @Override
    public double calcularSalario() {
        return getSalarioBase() + comissao;
    }
}
