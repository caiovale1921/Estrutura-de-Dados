while True:
    try:
        numero = int(input('Insira um numero de até 3 casas: '))
        if (len(str(numero)) > 3):
            raise(Exception('Insira um numero menor'))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'''
Centena: {((numero // 10) // 10) % 10}
Dezena : {(numero // 10) % 10}
Unidade: {numero % 10}
''')