import time
valor = int(input('Digite um número:'))
print('*'*20)
for m in range(1, 11,):
    print(f'{valor} x {m} = {valor * m}')
    time.sleep(0.5)
print('TE AMO!')
