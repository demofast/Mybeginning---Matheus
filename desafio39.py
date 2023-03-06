from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento:'))
idade = atual - ano
print(f'Você possui {idade} anos')
if idade == 18:
    print('Você precisa se alistar, compareça')
elif idade > 18:
    print(
        f'Você está com {idade -18} anos de atraso, favor compareça a junta')
else:
    print(f'Ainda faltam {18 - idade} anos para o ano do seu alistamento.')
