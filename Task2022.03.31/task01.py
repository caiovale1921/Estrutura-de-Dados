# Crie um vetor com 1000 posições ordenado.
# Faça um contador para determinar quantas vezes o laço de repetição mais interno (onde são feitas as trocas de valores) são executados nos quatro algoritmos.

# Métodos já modificados

def bubbleSort(self, vetor):
    for i in range(len(vetor) - 1 , 0, - 1):
        for i in range(i):
            if vetor[i] > vetor[i + 1]:
                aux = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = aux


import random

vetor = []

for i in range(0, 1000):
    vetor.append(random.randint(1,52))

print(vetor)