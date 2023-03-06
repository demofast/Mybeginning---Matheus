import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente; '))
hip = co**2 + ca**2 
raiz = math.sqrt(hip)
#Pode ser feito com hypot que é a funçao da hipotenusa
#math.hypot(co, ca)
print('O valor da hipotenusa é: {:.2f} '.format(raiz))