print('='*100)
casa = float(input('Qual o valor da casa que você deseja?'))
anos = int(input('Em quantos anos você vai pagar?'))
salario = float(input('Defina o seu salário atual: R$'))

prestaçao = casa / (anos * 12)
minimo = salario * 0.3
print(
    f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestaçao:.2f} ')
if minimo <= prestaçao:
    print('\33[1;30;41mPAGAMENTO NÃO APROVADO \33[m')
else:
    print('\33[1;30;42mPAGAMENTO APROVADO\33[m')


# #IDEIA DE UM ALUNO (GOSTEI) usou música.
# # importação
# import pygame

# # Inserção de dados
# salário = int(input('Qual é o seu salário? R$'))
# valor = int(input('Qual o valor da casa que quer financiar? R$'))
# tempo = int(input('Em quantos anos vai pagar?'))

# # calculos
# minimo = salário*0.3
# total = valor * (1 + 0.03)**tempo
# prestacao = total / (tempo * 12)

# # condições

# if minimo >= prestacao:
#     print('\33[1:32mFiNANCIAMENTO APROVADO!')
#     print(f'Você irá pagar R$ {prestacao:.2f} por mês')
#     print(f'Total do financialento: R$ {total:.2f}')

#     pygame.mixer.init()
#     pygame.mixer.music.load('Sino Longo.mp3')
#     pygame.mixer.music.play()
#     input()
#     pygame.event.wait()

# else:
#     print(
#         '\033[1:31mFINANCIAMENTO NÃO APROVADO!!, mensalidade superior a 30% do salário.')
#     pygame.mixer.init()
#     pygame.mixer.music.load('Triste.mp3')
#     pygame.mixer.music.play()
#     input()
#     pygame.event.wait()
