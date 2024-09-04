package Java.poo.agrupamento;

public class Pedido {
    private int numero;
    private TipoPrato prato;

    public Pedido(int numero, TipoPrato prato) {
        if (numero <= 0) {
            throw new IllegalArgumentException("Número do pedido deve ser positivo.");
        }
        if (prato == null) {
            throw new IllegalArgumentException("Nome do prato não pode ser vazio.");
        }
        this.numero = numero;
        this.prato = prato;
    }

    public int getNumero() {
        return this.numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public TipoPrato getPrato() {
        return this.prato;
    }

    public void setPrato(TipoPrato prato) {
        this.prato = prato;
    }

    @Override
    public String toString() {
        return "Pedido #" + numero + ": " + prato;
    }
}
