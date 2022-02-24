while True:
    try:
        peso = float(input('Insira seu peso: '))
        altura = float(input('Insira sus altura: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'Precisa de {((25 * (altura ** 2)) - peso):.2f} KG') 