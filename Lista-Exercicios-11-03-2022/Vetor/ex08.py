lista = []

for i in range(0, 20):
    numero = int(input('Insira um valor no vetor: '))
    if numero < 0 or numero > 2:
        break
    lista.append(numero)

for j in range(0, len(lista)):
    for i in range(0, len(lista) - 1):
        aux = 0
        if lista[i] > lista[i + 1]:
            aux = lista[i + 1]
            lista [i + 1] = lista[i]
            lista [i] = aux

print(f'Jeito Dificil: {lista}')

lista.sort()

print(f'Jeito Facil: {lista}')