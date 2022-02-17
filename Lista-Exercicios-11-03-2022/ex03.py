while True:
    try:
        qtdPaes = int(input("Insira a quantidade de pães vendidos:"))
        qtdBroas = int(input("Insira a quantidade de broas vendidos:"))
        break
    except Exception as ex:
        print('Ocorreu um erro, digite os valores novamente | Erro: ', ex)

totalArrecadado = (qtdBroas * 1.50) + (qtdPaes * 0.12)

totalParaPoupanca = totalArrecadado * 0.1

print(f'''
Total de Pães: {qtdPaes}\n
Total de Broas: {qtdPaes}\n
Total Arrecadado: R$ {totalArrecadado}\n
Total Para a poupança: R$ {totalParaPoupanca}
''')