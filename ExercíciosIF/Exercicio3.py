num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    crescente = (num1, num2)
    decrescente = (num2, num1)
else:
    crescente = (num2, num1)
    decrescente = (num1, num2)


print(f"Crescente: {crescente[0]}, {crescente[1]}")
print(f"Decrescente: {decrescente[0]}, {decrescente[1]}")
