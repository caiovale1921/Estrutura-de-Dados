nome = str(input('Insira seu nome: '))

while True:
    try:
        idade = int(input('Insira sua idade: '))
        break
    except Exception as ex:
        print('Ocorreu um erro | Erro: ', ex)

print(f'{nome}, você já viveu {idade * 365} anos')
