

menu = f'''
Bem vindo ao seu banco DigiLulis\n

Por favor, escolha uma das seguintes opções:

1 - Depósito
2 - Saque
3 - Extrato
0 - Sair

=>  '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 3
LIMITE_SAQUE = 3

while True:
    escolha = int(input(menu))
    
    if escolha == 1:
        
        deposito = int(input('Qual valor deseja depositar? '))
        if deposito > 0:

            print(f'O valor depositado foi de {deposito}')
            saldo += deposito
        else:
            print('Operação invalida')

    elif escolha == 2:
        saque = int(input('Qual valor deseja sacar? '))
        saldo -= saque
        print(f'Seu novo saldo e de {saldo}')

    elif escolha == 3:
        print('Extrato')

    elif escolha == 0:
        print('Saindo...')
        break
    else:
        print('Opcão invalida')