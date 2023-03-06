velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Excedeu limite de velocidade.')
    multa = (velocidade-80) * 7
    print('Sua multa é de {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
