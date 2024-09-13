nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7.0 and media <= 10.0:
    print("O aluno %s foi aprovado com media %.1f" % (nome, media))
elif media <7.0:
    print(f"O aluno {nome} foi reprovado com media {media}")
else:
    print("Media inválida")