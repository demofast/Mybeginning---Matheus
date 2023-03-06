a = int(input('Primeiro termo da PA: ').strip())
b = int(input('Razão da PA: ').strip())
c = a
contador = 1
while contador <= 10:
    print(f'{a}, ', end='')
    a += b
    contador += 1

print('Fim')
a_mais = int(input('Deseja ver mais quantos termos? '))
while a_mais > 0:
    contador = 1
    while contador <= a_mais:
        print(f'{a}, ', end='')
        a += b
        contador += 1
    a_mais = int(input('Deseja ver mais quantos termos? '))

print('Programa finalizado.')
