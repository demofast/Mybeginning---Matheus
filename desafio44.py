print('\33[1;97;45mLOJAS MAGAZINE LETICIA\33[m')

valor = float(input('Qual valor você irá pagar?'))

avista10 = valor - (valor * 0.10)
avista5 = valor - (valor * 0.05)
em2x = valor / 2
em3x = valor + (valor * 0.20)

forma = int(input('''Digite a forma de pagamento:
[1]A vista DINHEIRO/CHEQUE/PIX
[2]A vista CARTÃO CRED/DEB
[3]Em 2x SEM JUROS
[4]Em 3x ou mais
FORMA DE PAGAMENTO:'''))

if forma == 1:
    print(
        f'Você ganha 10% de desconto totalizando um valor de R$ {avista10:.2f}')
elif forma == 2:
    print(
        f'Você ganha 5% de desconto totalizando um valor de R$ {avista5:.2f}')
elif forma == 3:
    print(f'Você pagará 2x de R$ {em2x:.2f}')
else:
    print(f'''Você pagará 3x ou mais com um acrescimo de 20% no valor do produto: 
    Em [3x] de R$ {em3x / 3:.2f}
    Em [4x] de R$ {em3x / 4:.2f}
    Em [5x] de R$ {em3x / 5:.2f}
    Em [6x] de R$ {em3x / 6:.2f}
    Em [7x] de R$ {em3x / 7:.2f}
    Em [8x] de R$ {em3x / 8:.2f}
    Em [9x] de R$ {em3x / 9:.2f}
    Em [10x] de R$ {em3x / 10:.2f}
    Em [11x] de R$ {em3x / 11:.2f}
    Em [12x] de R$ {em3x / 12:.2f}''')

print('\33[1;97;45mBOAS COMPRAS\33[m')
