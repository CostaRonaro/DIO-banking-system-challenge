from typing import Final

balance = 0
WITHDRAW_LIMIT: Final = 3
withdraw_number = 0
LIMIT: Final = 500
extract = ''
saque_ext = ''
deposito_ext = ''

menu = """
##### MENU #####

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

################
=> """

while True:
    option = input(menu)

    if option == '1':
        print("Depositar")
        deposito = float(input('Informe valor a ser depositado: '))
        if deposito > 0 :
            balance += deposito
            deposito_ext += f'Deposito:........ R${deposito}\n'
        else:
            print('O valor depositado deve ser maior que 0')
        print(f'balance >> {balance}')

    elif option == '2':
        if withdraw_number <= WITHDRAW_LIMIT:
            print("Sacar")
            saque = float(input('Informe valor a ser sacado: '))
            if saque <= balance:
                if saque <= LIMIT:
                    balance -= saque
                    withdraw_number += 1
                    print(f'Saque de R${saque}')
                    saque_ext += f'Saque:........ R${saque}\n'
                else:
                    print(f'Você pode sacar até R${LIMIT} por saque.')
            else:
                print(f'Seu saldo é de R${balance}.\nSeu valor de saque não pode ser maior que o seu saldo!')
        else:
            print('Você atingiu o limite de saque diário')

    elif option == '3':
        balance_ext = f'Saldo:.......... R${balance}'
        print("Extrato")
        if balance > 0:
            extract = f"""
            \n========= EXTRATO =========

            \n{saque_ext}
            \n{deposito_ext}
            \n{balance_ext}

            \n===========================
            """
            print(extract)
        else:
            print('Não foram realizadas movimentações.')
        
    elif option == '0':
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione uma operação válida")
