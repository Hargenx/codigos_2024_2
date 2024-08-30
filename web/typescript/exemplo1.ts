let mensidadem: string = "Olá, TypeScript!";
const numero: number = 10;

console.log(mensidadem, numero)

function soma(a: number, b: number): number {
    return a + b;
}

// Uso da função
const resultado = soma(5, 10); // Resultado: 15

function apresenta(nome: string, apresenta: string = "Ola"): string {
    return `${apresenta}, ${nome}!`;
}

console.log(apresenta("Raphael")); // Saída: Olá, Raphael!
console.log(apresenta("Raphael", "Oi")); // Saída: Oi, Raphael!


/*interface Pessoa {
    nome: string;
    idade: number;
}

function printPessoa(pessoa: Pessoa): void {
    console.log(`nome: ${pessoa.nome}, idade: ${pessoa.idade}`);
}

const user: Pessoa = { nome: "Raphael", idade: 40 };
printPessoa(user); // Saída: nome: Raphael, idade: 40
*/

class Pessoa {
    protected nome: string;

    constructor(nome: string) {
        this.nome = nome;
    }

    public apresenta(): void {
        console.log(`Olá meu nome é ${this.nome} sou um aluno.`);
    }
}

class AlunoTecnico extends Pessoa {
    private grau: number;
    constructor(nome: string, grau: number = 0) {
        super(nome);
        this.grau = grau;
    }

    public apresenta(): void {
        console.log(`Olá meu nome é ${this.nome} e sou um técnico e estou no ${this.grau}º.`);
    }
}

const aluno = new AlunoTecnico("Raphael");
aluno.apresenta(); // Saída: Olá meu nome é Raphael e sou um técnico e estou no 0º.


type Direcao = "esquerda" | "direita" | "cima" | "baixo";
let mover: Direcao;
mover = "esquerda"; // Válido
// mover = "frente"; // Inválido


enum Status {
    Ativo = "Ativo",
    Inativo = "Inativo",
    Parado = "Parado",
}

let statusAtual: Status = Status.Ativo;
console.log(statusAtual); // Saída: Ativo



function identidade<T>(arg: T): T {
    return arg;
}

console.log(identidade<number>(42)); // Saída: 42
console.log(identidade<string>("Olá")); // Saída: Olá
