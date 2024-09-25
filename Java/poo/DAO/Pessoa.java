package Java.poo.DAO;

import java.util.Objects;

public class Pessoa {
    private int id;
    private String nome;
    private int idade;
    private float altura;

    public Pessoa() {
    }

    public Pessoa(int id, String nome, int idade, float altura) {
        this.id = id;
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float getAltura() {
        return this.altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public Pessoa id(int id) {
        setId(id);
        return this;
    }

    public Pessoa nome(String nome) {
        setNome(nome);
        return this;
    }

    public Pessoa idade(int idade) {
        setIdade(idade);
        return this;
    }

    public Pessoa altura(float altura) {
        setAltura(altura);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Pessoa)) {
            return false;
        }
        Pessoa pessoa = (Pessoa) o;
        return id == pessoa.id && Objects.equals(nome, pessoa.nome) && idade == pessoa.idade && altura == pessoa.altura;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, nome, idade, altura);
    }

    @Override
    public String toString() {
        return "{" +
                " id='" + getId() + "'" +
                ", nome='" + getNome() + "'" +
                ", idade='" + getIdade() + "'" +
                ", altura='" + getAltura() + "'" +
                "}";
    }

}
