numeros = [10,15,20,25,30,14,20,19,34,14,20,12]
print(list(enumerate(numeros)))
for i in enumerate(numeros, start=6):
    print(f"Indice -> {i[0]} - valor -> {i[1]}")
