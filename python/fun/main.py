import sys
import random

u = int(sys.argv[1])  # Input number
r = random.randint(0, 10000)  # Random number
a = [0] * 10000  # Array initialized to 0

# Precomputar a soma de j % u para j em 0 até 99999
mod_sum = sum(j % u for j in range(100000))

# Adicionar essa soma pré-calculada em cada elemento do array
for i in range(10000):
    a[i] = mod_sum + random.randint(0, 10000)

# Exibir o valor do índice aleatório
print(a[r])
