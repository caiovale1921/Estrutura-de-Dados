while True:
    try:
        diasSemAcidentes = int(input('Insira a quantidade de dias sem acidentes: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'''Total da contagem em:
Dias: {diasSemAcidentes:.2f}
Meses: {(diasSemAcidentes / 30):.2f}
Anos: {(diasSemAcidentes / 365):.2f}
''')