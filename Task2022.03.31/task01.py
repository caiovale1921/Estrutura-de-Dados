# Crie um vetor com 1000 posições ordenado.
# Faça um contador para determinar quantas vezes o laço de repetição mais interno (onde são feitas as trocas de valores) são executados nos quatro algoritmos.

import random

vetor = []

for i in range(0, 1000):
    vetor.append(random.randint(1,52))

print(vetor)