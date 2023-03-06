nota = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

média = (nota + nota2)/2

print(f'A média da suas notas é de {média} e você está:')

if média < 5.0:
    print('REPROVADO')
elif média >= 5.0 and média < 7.0:
    print('EM RECUPERAÇÃO')
else:
    print('APROVADO!!!')
