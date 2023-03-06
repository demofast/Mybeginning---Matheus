numero = int(input('Digite aqui um número inteiro:'))
print('''Escolha o tipo de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
[4] MOSTRAR TODOS OS RESULDADOS''')
opçao = int(input('Digite a opção desejada:'))

if opçao == 1:
    print(f'O número {numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opçao == 2:
    print(f'O número {numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opçao == 3:
    print(
        f'O número {numero} convertido para HEXADECIMAL é: {hex(numero)[2:]}')
elif opçao == 4:
    print(
        f'''Resposta dos 3 tipos {bin(numero), oct(numero), hex(numero)[2:]}''')
else:
    print('Opção inválida, digite novamente!')
