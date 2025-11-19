n = int(input("Limite: "))
perfeitos = 0

for num in range(1, n+1):
    soma = 0
    for d in range(1, num):
        if num % d == 0:
            soma += d
    if soma == num:
        perfeitos += 1

print("Quantidade de números perfeitos:", perfeitos)
