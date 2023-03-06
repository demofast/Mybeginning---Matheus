num = int(input('Digite um número:'))
total = 0
for m in range(1, num + 1):
    if num % m == 0:
        print('\33[34m', end='')
        total += 1
    else:
        print('\33[32m', end='')
    print(f'{m}', end=' ')
print(f'\n\33[33m O número {num} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
