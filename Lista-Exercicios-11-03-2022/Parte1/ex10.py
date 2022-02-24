from math import sqrt

while True:
    try:
        x = []
        y = []
        for i in range(2):
            x.append(float(input(f'Insira o valor {i + 1} de X: ')))
        for i in range(2):
            y.append(float(input(f'Insira o valor {i + 1} de Y: ')))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'A distancia entre os pontos é de: {sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)}')