soma = 0
count = 0

for m in range(1, 7):
    n = int(input('Digite qualquer número:'))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'A soma dos valores pares são {soma}')
