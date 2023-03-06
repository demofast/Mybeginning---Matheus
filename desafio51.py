# Fiquei travado
primeiro = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
termo = primeiro + (10 - 1) * razão
for m in range(primeiro, termo + razão, razão):
    print(f'{m}', end=' ')
print('ACABOU')
