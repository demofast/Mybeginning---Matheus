n = int(input("Digite o número de elementos da sequência de Fibonacci: "))

fibonacci = [0, 1]

if n <= 2:
    print(fibonacci[:n])
else:
    for i in range(2, n):
        proximo = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo)
    print(fibonacci)
