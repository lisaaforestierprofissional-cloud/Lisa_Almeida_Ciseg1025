n = int(input("Número: "))
contador = 0

for i in range(1, n+1):
    if n % i == 0:
        contador += 1

print("Número de divisores:", contador)
