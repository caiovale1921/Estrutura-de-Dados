#Algoritimo realizado de modo genérico, capaz de calcular com qualquer quantidade de notas/pesos
while True:
    try:
        notas = []
        for i in range(int(input('Insira a quantidade de pesos: '))):
            notas.append(float(input(f'Insira a nota {i + 1}: ')))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

pesos = 0
totalNota = 0
for i in range(len(notas)):
    totalNota += notas[i] * (i + 1)
    pesos += (i + 1)

print(f'A média ponderada é: {totalNota / pesos}')