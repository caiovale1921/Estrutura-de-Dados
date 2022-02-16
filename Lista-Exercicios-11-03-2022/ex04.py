while True:
    try:
        valorGasolina = float(input('Insira o valor da gasolina por Litro: '))
        valorAColocar = float(input('Insira o quanto de gasolina deseja colocar: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'Você consegue abastecer: {valorAColocar / valorGasolina} Litros')