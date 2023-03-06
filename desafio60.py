# num = int(input('Fatorial de:'))
# resultado = 1
# count = 1

# while count <= num:
#     resultado *= count
#     count += 1

# print(resultado)

num = int(input('Fatorial de:'))
c = num
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='',)
    f *= c
    c -= 1
print(f'{f}')
