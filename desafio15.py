km = int(input('Quantos quilometros o carro percorreu? ' ))
dias = int(input('Quantos dias de aluguel? '))
valor = (60 * dias) + (0.15 * km)
print('O valor a ser pago é: R$ {}'.format(valor))