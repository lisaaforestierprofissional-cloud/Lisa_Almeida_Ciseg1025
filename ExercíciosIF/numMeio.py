num1 = int(input("Introduz o 1º número: "))
num2 = int(input("Introduz o 2º número: "))
num3 = int(input("Introduz o 3º número: "))

if num1 == num2 == num3:
    print("Todos são iguais.")
else:
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    meio = (num1 + num2 + num3) - maior - menor

    print(f"O maior número é {maior}, o menor número é {menor}, e o número do meio é {meio}.")
