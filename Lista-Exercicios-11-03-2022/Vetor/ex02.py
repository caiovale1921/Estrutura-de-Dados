lista = []

for j in range(0, 10):
    lista.append(input(f'Insira o numero {j + 1 } da lista: '))

listaReversa = list(reversed(lista))

print('Lista normal: ', lista)
print('Lista Inversa: ', listaReversa)
