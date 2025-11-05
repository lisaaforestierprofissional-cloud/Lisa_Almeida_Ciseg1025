num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]

crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)

print(f"Crescente: {crescente[0]}, {crescente[1]}, {crescente[2]}")
print(f"Decrescente: {decrescente[0]}, {decrescente[1]}, {decrescente[2]}")
