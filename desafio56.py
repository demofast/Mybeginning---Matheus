soma_idade = 0
média_idade = 0
maior_idade = 0
nome_velho = ''
menosde20 = 0

for pess in range(1, 5):
    print(f'-----{pess}ª PESSOA------')
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma_idade += idade
    if pess == 1 and sexo == 'M':
        maior_idade = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if idade < 20 and sexo == 'F':
        menosde20 += 1
média_idade = soma_idade / 4
print(f'A média das idades é {média_idade}')
print(f'O homem mais velho tem {maior_idade} e se chama {nome_velho}')
print(f'Somente {menosde20} melheres tem menos de 20 anos')
