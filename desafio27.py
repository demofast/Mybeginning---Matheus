nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('O seu nome é {} '.format(nome))
print('O seu primeiro nome é: {}'.format(n[0]))
print('O seu primeiro nome é: {}'.format(n[len(n)-1]))
