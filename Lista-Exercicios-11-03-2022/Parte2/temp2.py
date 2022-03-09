
# Permita a digitação de vários numeros (-1 interrompe a leitura),
# calcule e mostre a média dos numeros digitados

i = 0
numeros = []
while True:
    input = int(input(f'Insira o numero {i}: '))
    if (input == -1):
        break
    numeros.append(input)
