while True:
    try:
        dia = int(input('Insira o dia do mês: '))
        if dia > 30 or dia < 1:
            raise(Exception('Dia Invalido'))
        mes = int(input('Insira o mês: '))
        if mes > 12 or mes < 1:
            raise(Exception('Mês Inválido'))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'Já se passaram {(mes - 1) * 30 + dia} dias desde o começo do ano')