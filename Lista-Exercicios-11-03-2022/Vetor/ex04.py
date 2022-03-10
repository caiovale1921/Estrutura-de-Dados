palavra = str(input('Insira uma palavra: '))

isPalindromo = False

for i in range(0, int(len(palavra) // 2)):
    if (palavra[i] == palavra[(len(palavra) - 1) - i]):
        isPalindromo = True
    else:
        isPalindromo = False
        break

if isPalindromo:
    print(f'A palavra {palavra}, é um palindromo')
else:
    print(f'A palavra {palavra}, não é um palindromo')