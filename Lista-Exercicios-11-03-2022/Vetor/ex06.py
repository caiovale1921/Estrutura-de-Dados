lista1 = []
lista2 = []

while True:
    numero = int(input('Insira um numero no vetor 1 - NUMERO NEGATIVO SAI: '))
    if numero < 0:
        break
    lista1.append(numero)

while True:
    numero = int(input('Insira um numero no vetor 2 - NUMERO NEGATIVO SAI: '))
    if numero < 0:
        break
    lista2.append(numero)

if (len((set(lista1) & set(lista2))) == len(lista1)):
    print('Lista com conteudos iguais')
else:
    print('Lista com conteudos diferentes')
