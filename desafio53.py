frase = str(input('Digite a frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'{frase} É um palíndromo: {inverso}')
else:
    print(f'{frase} Não é um palíndromo: {inverso}')
