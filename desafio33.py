a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
if a < b and a < c:  # É possivel fazer tanto assim
    menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
maior = a  # Quanto assim.
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
