lista = []

for i in range(0, 20):
    lista.append(int(input('Insira um valor no vetor: ')))

for j in range(0, len(lista)):
    for i in range(0, len(lista) - 1):
        aux = 0
        if lista[i] > lista[i + 1]:
            aux = lista[i + 1]
            lista [i + 1] = lista[i]
            lista [i] = aux

print(f'Vetor ordenado: {lista}')