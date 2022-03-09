lista1 = []
lista2 = []

for i in range(0, 10):
    lista1.append(int(input(f'Insira um valor na posição {i + 1} do vetor: ')))

for j in range(0, 10):
    if (lista1[j] % 2) == 0:
        lista2.append(lista1[j] / 2)
    else:
        lista2.append(lista1[j] * 3)

print(lista1)
print(lista2)