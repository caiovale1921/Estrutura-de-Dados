lista = []

while True:
    numero = int(input('Insira um valor para o vetor: '))
    if numero == - 1:
        break
    lista.append(numero)

pares = []
somaPares = 0
impares = []
somaImpares = 0
for i in lista:
    if (i % 2) == 0:
        pares.append(i)
        somaPares += i
    else:
        impares.append(i)
        somaImpares += i

print(f'Pares: {pares}\nSomatório: {somaPares}')
print(f'Impares: {impares}\nSomatório: {somaImpares}')
