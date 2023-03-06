# tempo = int(input('Qual a idade do seu carro? '))
# if tempo <= 5:
#     print('Carro novo ou seminovo')
# else:
#     print('Carro velho')

from random import randint

computador = randint(0, 5)  # faz o computador randerizar "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Qual número eu estou pensando? '))
print('Pensei no número {}'.format(computador))
if jogador == computador:
    print('PARABÉNS! Você venceu.')
else:
    print('HAHA! Eu ganhei, você foi derrotado')
