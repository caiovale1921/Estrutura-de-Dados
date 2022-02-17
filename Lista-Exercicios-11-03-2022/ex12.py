while True:
    try:
        salario = float(input('Insira o salário do funcionário: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'''Calculo de salário:
Salario Inicial: {salario}
Salario Final: {(salario + (salario * 0.15)) - ((salario + (salario * 0.15)) - (salario * 0.08))}
''')