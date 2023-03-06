distancia = float(input('Digite a distância que você irá percorrer:'))
if distancia > 200:
    preço = distancia * 0.45
else:
    preço = distancia * 0.50
print('O preço da sua passagem é de R${:.2f}'.format(preço))
