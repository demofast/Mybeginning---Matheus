# Um tanto complicado no primeiro contato, voltar e resolver de diversas formas.


sexo = str(input('Digite o seu sexo: ')).strip().upper()
while not sexo == 'M' and not sexo == 'F':
    sexo = str(input('Sexo inválido, digite novamente:')).strip().upper()
print(f'Sexo {sexo} registrado com súcesso')
