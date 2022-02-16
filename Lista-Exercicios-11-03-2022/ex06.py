while True:
    try:
        valorBalanca = float(input('Insira o peso do prato: '))
        break
    except Exception as ex:
        print('Ocorre um erro | Erro: ', ex)

print(f'Valor da comida: R$ {12 * valorBalanca}')