def selectionSort(vetor):

    for i in range(0, len(vetor) - 1):
        for j in range(i + 1, len(vetor)):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor

v = [1, 6, 8, 4, 2, 1]
print('teste')

print(selectionSort(v))