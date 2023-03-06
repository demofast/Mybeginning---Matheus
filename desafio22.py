nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {} '.format(nome.upper()))
print('Seu nome em minúsculo é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome possui {} letras '.format(nome.find(' ')))

# ou pode ser feito da seguinte forma:

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(
    separa[0], len(separa[0])))

# neste desafio foi ensinado como trabalhar uma frase de formas variadas. exercício da
