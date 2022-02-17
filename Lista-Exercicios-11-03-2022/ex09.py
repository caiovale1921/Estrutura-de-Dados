while True:
    try:
        qtdPequena = int(input('Insira a quantidade de camisas PEQUENAS: '))
        qtdMedia = int(input('Insira a quantidade de camisas MÉDIAS: '))
        qtdGrande = int(input('Insira a quantidade de camisas GRANDES: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'Total arrecado foi: R$ {(qtdPequena * 10) + (qtdMedia * 12) + (qtdGrande * 15)}')