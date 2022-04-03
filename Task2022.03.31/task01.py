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
        count += 1  
        while j >= 0 and aux < vetor[j]:
            vetor[j + 1] = vetor[j]
            j = j - 1
            
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
            count += 1
            while j >= 0 and atual < vetor[j]:
                vetor[j + h] = vetor[j]
                j = j - h
            vetor[j + h ] = atual
    return count

# Código principal

import random

vetor = []

while True:
    print('Vetor ordenado: ', vetor)
    vetor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Vetor desrodenado: ', vetor)
    #for i in range(0, 10):
    #    vetor.append(random.randint(1,52))
    menu = int(input('''Escolha o método de ordenação:\n1 - BubbleSort\n2 - Insertion Sort\n3 - Selection Sort\n4 - Shell Sort\n\n'''))
    if menu == 1:
        print('\n\nBubbleSort - Rodou: ', bubbleSortMetric(vetor), '\n\n')
    elif menu == 2:
        print('\n\nSelection Sort - Rodou: ', selectionSortMetric(vetor), '\n\n')
    elif menu == 3:
        print('\n\nInsertion Sort - Rodou: ', insertionSortMetric(vetor), '\n\n')
    elif menu == 4:
        print('\n\nShell Sort - Rodou: ', shellSortMetric(vetor), '\n\n')