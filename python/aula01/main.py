def entrada_dados() -> tuple:
    fez = input("O aluno fez a prova 1? (Sim/Não): ")
    if fez == "Sim" or "sim":
        nota1 = float(input("Digite a nota da prova 1: "))
    else:
        nota1 = None

    nota2 = float(input("Digite a nota da prova 2: "))
    
    if nota1 is not None:
        nota_final = verifica_nota(nota1, nota2)
    else:
        nota_final = nota2 / 2
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade, nota_final

def verifica_nota(nota1: float, nota2: float) -> float:
    return (nota1 + nota2) / 2

def condicao(nota_final: float) -> bool:
    if 4 <= nota_final <= 6:
        return True
    return False

if __name__ == "__main__":
    nome, idade, nota_final = entrada_dados()
    if condicao(nota_final):
        print("Nota final está entre 4 e 6")
    else:
        print("Nota final não está entre 4 e 6")
    print(f"Nome: {nome} | Idade: {idade} | Nota Final: {nota_final}")
