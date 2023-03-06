peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu imc é de {imc:.2f} e voce está abaixo do peso')
elif imc <= 25:
    print(f'Seu imc é de {imc:.2f} e voce está no peso ideal')
elif imc <= 30:
    print(f'Seu imc é de {imc:.2f} e voce está sobrepeso')
elif imc <= 40:
    print(f'Seu imc é de {imc:.2f} e voce está com obesidade, CUIDE-SE')
else:
    print(
        f'Seu imc é de {imc:.2f} e voce está com obesidade morbida, CUIDE-SE')
