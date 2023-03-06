import random
maquina = random.randint(0, 10)
jogador = -1
count = 0
while not jogador == maquina:
    jogador = int(input('Digite um número: '))
    count += 1
print(f'Pensei no número: {maquina}')

if count != 0:
    print(f'Você levou {count} tentativas para acertar.')
