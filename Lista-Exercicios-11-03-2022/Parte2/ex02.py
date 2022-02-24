peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)

print(f'Seu imc é: {imc:.2f}')

if (imc < 18.5):
    print('Abaixo do peso')
elif (imc < 25):
    print('Peso Normal')
elif (imc < 30):
    print('Sobrepeso')
elif (imc < 40):
    print('Obeso Moderado')
else:
    print('Gordão demais')