lista = []

for j in range(0, 10):
    lista.append(input(f'Insira o numero {j + 1 } da lista: '))

i = 0
i2 = len(lista)
while True:  
    print(f'{lista[i]} -- {lista[i2 - 1]}')
    i += 1
    i2 -= 1
    if (i2 == 0):
        break
        