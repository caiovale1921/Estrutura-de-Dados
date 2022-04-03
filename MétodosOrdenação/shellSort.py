def shellSort(vetor):
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
            vetor[j + h ] = atual