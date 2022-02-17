saldo = 0

while True:
    try:

        menu = str(input(f'''
        Selecione o tipo de operação:\n 
        1 - Depósito\n
        2 - Saque\n
        3 - Extrato\n
        4 - Sair\n
        Saldo -> {saldo}
        '''))

        if (menu == '1'): #Depósito
            saldo += float(input("Insira o valor a ser depositado: "))
        elif(menu == '2'): #Saque
            saldo -= float(input("Insira o valor a ser sacado: "))
        elif(menu == '3'): #Extrato
            if (saldo > 0): #Saldo Positivo
                print(f"Saldo: R$ {saldo} | Positivo\n")
            elif (saldo < 0): #Saldo Negativo
                print(f"Saldo: R$ {saldo} | Negativo\n")
            else: #Saldo Zerado
                print('Saldo Zerado\n')
        elif (menu == '4'): #sair
            break
        else:
            print('Operação Invalida')

    except:
        print('Ocorreu um erro - Tente Novamente')
        
