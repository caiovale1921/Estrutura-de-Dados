# Crie um vetor com 1000 posições ordenado.
# Faça um contador para determinar quantas vezes o laço de repetição mais interno (onde são feitas as trocas de valores) são executados nos quatro algoritmos.

# Métodos já modificados

def bubbleSortMetric(vetor):
    count = 0
    for i in range(len(vetor) - 1 , 0, - 1):
        for i in range(i):
            count += 1
            if vetor[i] > vetor[i + 1]:
                aux = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = aux
                
    return count

def selectionSortMetric(vetor):
    count = 0
    for i in range(0, len(vetor) - 1):
        for j in range(i + 1, len(vetor)):
            count += 1
            if vetor[i] > vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
                
    return count

def insertionSortMetric(vetor):
    count = 0
    for i in range(1, len(vetor)):
        aux = vetor[i]
        j = i - 1 
        while j >= 0 and aux < vetor[j]:
            vetor[j + 1] = vetor[j]
            j = j - 1
            count += 1
        vetor[j + 1] = aux
    return count

def shellSortMetric(vetor):
    count = 0
    h = 1
    n = len(vetor)
    while h < n:
        h = h * 3 + 1
    while h > 1:
        h = h // 3
        for i in range(h, n, h):
            atual = vetor[i]
            j = i - h
            while j >= 0 and atual < vetor[j]:
                vetor[j + h] = vetor[j]
                j = j - h
                count += 1
            vetor[j + h ] = atual
    return count

# Código principal

import os
import random

vetor = []

while True:
    vetor = []
    vetorSize = int(input('Escolha o tamanho do vetor: '))
    os.system('cls')

    vetorType = (int(input('1 - Vetor crescente\n2 - Vetor decrescente\n3 - Vetor Aleatório\nSelecione uma opção: ')))
    os.system('cls')

    if vetorType == 1:
        vetorOrder = 'Crescente'
        for i in range(0, vetorSize):
            vetor.append(i + 1)

    elif vetorType == 2:
        vetorOrder = 'Decrescente'
        for i in range(vetorSize,0 , -1):
            vetor.append(i)
    else:
        vetorOrder = 'Aleatório'
        for i in range(1, vetorSize):
            vetor.append(random.randint(1, 100))

    menu = int(input(f'''Vetor: {vetor}\nEscolha o método de ordenação:\n1 - BubbleSort\n2 - Insertion Sort\n3 - Selection Sort\n4 - Shell Sort\nSelecione uma opção: ({vetorOrder}) \n'''))
    
    if menu == 1:
        os.system('cls')
        print(f'BubbleSort - Quantidade de operações realizadas: {bubbleSortMetric(vetor)} - ({vetorOrder})\nVetor ordenado: {vetor}\n')
    elif menu == 2:
        os.system('cls')
        print(f'Selection Sort - Quantidade de operações realizadas: {selectionSortMetric(vetor)} - ({vetorOrder})\nVetor ordenado: {vetor}\n')
    elif menu == 3:
        os.system('cls')
        print(f'Insertion Sort - Quantidade de operações realizadas: {insertionSortMetric(vetor)} - ({vetorOrder})\n\Vetor ordenado: {vetor}n')
    elif menu == 4:
        os.system('cls')
        print(f'Shell Sort - Quantidade de operações realizadas: {shellSortMetric(vetor)} - ({vetorOrder})\nVetor ordenado: {vetor}\n')