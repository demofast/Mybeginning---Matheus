#preço = float(input('Digite o valor do item: R$'))
#desc = (preço * 95 / 100 )
#print('O valor com desconto é de R${:.2f} '.format(desc))

preço = float(input('Digite o valor do item: R$'))
desc = preço - (preço * 5 / 100)
print('O valor com desconto é de R${:.2f} '.format(desc))