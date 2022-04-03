def bubbleSort(self, vetor):
    for i in range(len(vetor) - 1 , 0, - 1):
        for i in range(i):
            if vetor[i] > vetor[i + 1]:
                aux = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = aux