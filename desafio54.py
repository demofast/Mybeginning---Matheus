from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pess}ª pessoa:'))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmaior} MAIORES')
print(f'{totmenor} MENORES')
