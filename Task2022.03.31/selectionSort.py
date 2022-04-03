def selectionSort(self, vetor):
    for i in range(0, len(vetor) - 1):
        for j in range(i + 1, len(vetor)):
            if vetor[i] > vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
    return vetor