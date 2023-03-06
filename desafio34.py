salario = float(input('Digite o seu salário R$:'))
if salario < 1250:
    aumento = salario * 0.15
if salario > 1250:
    aumento = salario * 0.10
print('Seu salário teve um aumento de R${}'.format(aumento))
print('O valor atual do seu salário é R${}'.format(aumento + salario))
