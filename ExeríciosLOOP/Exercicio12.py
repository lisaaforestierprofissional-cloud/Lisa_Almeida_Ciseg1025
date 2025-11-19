n = int(input("Digite um número: "))
operacoes = 0

for i in range(1, n):
    print(f"{n} + {i} = {n+i}")
    print(f"{n} - {i} = {n-i}")
    print(f"{n} * {i} = {n*i}")
    print(f"{n} / {i} = {n/i}")
    operacoes += 4

print("Total de operações:", operacoes)
