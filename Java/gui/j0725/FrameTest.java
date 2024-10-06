package j0725;

import java.awt.*;   // Importação do AWT para componentes gráficos
import javax.swing.*; // Importação do Swing para JFrame e outros componentes

class FrameTest {

    public static void main(String[] args) {
        // Criação do JFrame
        JFrame f = new JFrame("Minha Janela"); 
        
        // Definir a posição da janela
        f.setLocation(100, 100); // Exemplo de coordenadas X e Y

        // Definir o tamanho da janela
        f.setSize(600, 400); // Largura 600 e altura 400

        // Configurar para fechar o programa ao fechar a janela
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Tornar a janela visível
        f.setVisible(true);
    }
}
