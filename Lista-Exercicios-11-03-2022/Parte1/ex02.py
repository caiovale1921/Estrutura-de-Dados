while True:
    try:
        qtdCavalos = int(input('Insira a quantidade de cavalos comprados: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ',ex)

print(f'Total de ferraduras necessárias: {qtdCavalos * 4}')