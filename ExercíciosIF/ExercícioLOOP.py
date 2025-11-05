pares = 0
impares = 0


for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}º número: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Saída
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
