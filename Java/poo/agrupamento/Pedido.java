package Java.poo.agrupamento;

public class Pedido {
    private int numero;
    private String prato;

    public Pedido(int numero, String prato) {
        this.numero = numero;
        this.prato = prato;
    }

    public int getNumero() {
        return this.numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getPrato() {
        return this.prato;
    }

    public void setPrato(String prato) {
        this.prato = prato;
    }

    @Override
    public String toString() {
        return "Pedido #" + numero + ": " + prato;
    }
}
