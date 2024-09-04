package Java.poo.projeto;

import java.util.Date;

public class Aluno extends Pessoa {

    private String matricula;
    private float nota;
    private String turma;


    public Aluno() {
    }

    public Aluno(String nome, Date dataNascimento, String endereco, int telefone, String email, String matricula, float nota, String turma) {
        super(nome, dataNascimento, endereco, telefone, email);
        this.matricula = matricula;
        this.nota = nota;
        this.turma = turma;
    }


    public String getMatricula() {
        return this.matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public float getNota() {
        return this.nota;
    }

    public void setNota(float nota) {
        this.nota = nota;
    }

    public String getTurma() {
        return this.turma;
    }

    public void setTurma(String turma) {
        this.turma = turma;
    }

}
