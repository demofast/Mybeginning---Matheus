a = int(input('Primeiro termo da PA: ').strip())
b = int(input('Razão da PA: ').strip())
c = a
cont = 1
mais = 10
while a != c + 9 * b:
    a += b
    print(f'{a}, ', end='')
print('Fim')
a_mais = int(input('Deseja ver mais quantos termos?'))
