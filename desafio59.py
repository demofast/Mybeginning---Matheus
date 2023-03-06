import time
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
while num1 and num2:
    print('-='*40)
    menu = int(input('''MENU:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA
    Digite qual menu gostaria de usar: '''))
    print('-='*40)
    if menu == 1:
        print(f'Resultado: {num1 + num2:.2f}')
    elif menu == 2:
        print(f'Resultado: {num1 * num2:.2f}')
    elif menu == 3:
        if num1 > num2:
            print(f'O maior é {num1}')
        elif num1 < num2:
            print(f'O maior é {num2}')
        else:
            print('Os valores são iguais.')
    elif menu == 4:
        num1 = float(input('Digite novos números, 1º número: '))
        num2 = float(input('Digite o 2º número: '))
    elif menu == 5:
        print('Finalizando...')
        time.sleep(2)
        print('Você saiu do programa.')
        quit()
    else:
        print('Opção inválida, tente novamente.')
