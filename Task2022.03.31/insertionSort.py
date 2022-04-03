from tkinter.messagebox import RETRY


def insertionSort(self, vetor):
    for i in range(1, len(vetor)):
        aux = vetor[i]
        j = i - 1   
        while j >= 0 and aux < vetor[j]:
            vetor[j + 1] = vetor[j]
            j = j - 1
        vetor[j + 1] = aux
    return vetor