package Java.poo.tente;

public class ExemploThrow {
    public int foo(String x) throws NumberFormatException {
        return (Integer.parseInt(x)); // A assinatura do método diz que pode lançar uma NumberFormatException
    } // Mas o método não trata, ao invés disso lança a exceção com throws

    public void bar() throws NumberFormatException {
        try {
            int a = this.foo("x"); // Chama o método foo() que declara lançar uma exceção.
            System.out.println("String convertida em int é: " + a); // Este método deve ou capturar ou relançar a
                                                                    // exceção que recebeu.
        } catch (NumberFormatException e) { // Este catch captura a exceção.
            throw new NumberFormatException(); // Mas aqui dentro ele resolve relançar ela.
                                               // Usa throw, e new para criar o objeto. E, na assinatura deve haver
                                               // um throws.
        }
    }

    public static void main(String args[]) {
        try { // Esse aqui chama bar() que lança a exceção que pegou de foo.
            ExemploThrow teste = new ExemploThrow(); // Este deve ou capturar ou relançar.
            teste.bar();
        } catch (NumberFormatException e) { // Ele resolve capturar e fazer o tratamento necessário.
            System.out.println("Capturei a exceção lançada no método foo()"); // Final, encerrou a pilha de
                                                                              // propagação da exception.
            e.printStackTrace();
        }
    }
}
