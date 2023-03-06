from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade <= 25:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')
