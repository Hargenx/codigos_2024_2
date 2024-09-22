package Java.gravacao_texto;

import java.io.FileWriter;
import java.io.IOException;
import java.io.File;

public class Gravar {
    public static void main(String[] args) {
        // Diretório onde deseja criar o arquivo
        String subdiretorio = System.getProperty("user.dir") + System.getProperty("file.separator") + "Java"
                + System.getProperty("file.separator") + "gravacao_texto";
        System.out.println("Subdiretório: " + subdiretorio);

        // Certifique-se de que o subdiretório existe
        File diretorio = new File(subdiretorio);
        if (!diretorio.exists()) {
            diretorio.mkdirs(); // Cria o diretório se ele não existir
        }

        // Caminho completo do arquivo
        String caminhoArquivo = subdiretorio + System.getProperty("file.separator") + "arquivo.txt";
        System.out.println("Caminho completo do arquivo: " + caminhoArquivo);

        FileWriter escrever = null;

        try {
            File arquivo = new File(caminhoArquivo);

            // Cria o arquivo se ele não existir
            if (!arquivo.exists()) {
                arquivo.createNewFile();
            }

            escrever = new FileWriter(arquivo); // Aqui é onde o FileWriter cria o arquivo dentro do diretório
            escrever.write("Raphael");
            System.out.println("Arquivo gravado com sucesso em: " + caminhoArquivo);

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (escrever != null) {
                    escrever.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
