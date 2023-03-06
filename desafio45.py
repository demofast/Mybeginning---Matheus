from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-='*30)
print('👊🖐 ✌ JOGO DO JOKENPÔ 👊🖐 ✌')
print('-='*30)
print('''Suas opççoes:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador = int(input('Qual a sua jogada?'))

print('-='*30)
print(f'Jogador jogou {itens[jogador]}')
print(f'Computador jogou {itens[computador]}')
print('-='*30)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

# code de outro
# from random import choices
# from time import sleep
# c = choices(['PEDRA 👊', 'PAPEL 🖐', 'TESOURA ✌'])
# o = ['']

# print('=' * 16)
# print('👊🖐 ✌ JOGO DO JOKENPÔ 👊🖐 ✌')
# print('=' * 16)
# sleep(1)
# print('Escolha entre:\n[1] - PEDRA 👊\n[2] - PAPEL 🖐\n[3] - TESOURA ✌')
# print('=' * 16)
# print('')
# e = int(input(f'Digite: '))
# print('')
# sleep(0.3)

# if e == 1:
#     o = 'PEDRA 👊'
#     print(f'Você escolheu {o} e o computador escolheu {c}')
#     if o == c:
#         print(f'EMPATOU!')
#     elif c == 'PAPEL 🖐':
#         print('Você PERDEU!')
#     else:
#         print('você GANHOU!')
# elif e == 2:
#     o = 'PAPEL 🖐'
#     print(f'Você escolheu {o} e o computador escolheu {c}')
#     if o == c:
#         print(f'EMPATOU!')
#     elif c == 'TESOURA ✌':
#         print('você PERDEU!')
#     else:
#         print('Você GANHOU!')
# elif e == 3:
#     o = 'TESOURA ✌'
#     print(f'Você escolheu {o} e o computador escolheu {c}')
#     if o == c:
#         print('EMPATOU!')
#     elif c == 'PEDRA 👊':
#         print('Você PERDEU!')
#     else:
#         print('Você GANHOU!')
# else:
#     print('OPÇÃO INVÁLIDA!')

# code de outro
# import random
# print("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
# a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
# b = random.randint(1, 3)
# print(b)
# if a == b:
#     print("EMPATE")
# elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
#     print("VOCÊ PERDEU!")
# else:
#     print("VOCÊ GANHOU")
