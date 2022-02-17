while True:
    try:
        lados = []
        for i in range(2):
            lados.append(float(input('Insira os lados do retângulo: ')))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'A área do retângulo é: {lados[0] * lados[1]}')