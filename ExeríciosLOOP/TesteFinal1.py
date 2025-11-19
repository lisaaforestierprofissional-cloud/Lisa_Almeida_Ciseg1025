def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def contar_divisores(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    return c


def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

while True:
    valor = int(input("Digite um número entre 1 e 30000: "))
    if 1 <= valor <= 30000:
        break

print("\n--- Resultados ---\n")

contador = 0

for num in range(valor, 0, -1):
    primo = "Sim" if eh_primo(num) else "Não"
    divisores = contar_divisores(num)
    perfeito = "Sim" if eh_perfeito(num) else "Não"

    print(f"Número: {num}")
    print("Primo:", primo)
    print("Divisores:", divisores)
    print("Perfeito:", perfeito)
    print("-" * 30)

    contador += 1
    if contador % 10 == 0:
        c = input("Continuar? (s/n): ")
        if c.lower() != "s":
            break

def tabuada(n):
    print(f"\nTabuada do {n} até {n}:")
    for i in range(1, n+1):
        print(f"{n} x {i} = {n*i}")
        if i % 20 == 0:
            c = input("Continuar? (s/n): ")
            if c.lower() != "s":
                break


while True:
    print("""
----- MENU -----
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Tabuada
0 - Sair
""")

    op = input("Opção: ")

    if op == "0":
        break

    a = int(input("Digite o primeiro número (1-1000): "))
    b = int(input("Digite o segundo número (1-1000): "))

    if not (1 <= a <= 1000 and 1 <= b <= 1000):
        print("Valores inválidos.")
        continue

    if op == "1":
        print("Resultado:", a + b)
    elif op == "2":
        print("Resultado:", a - b)
    elif op == "3":
        print("Resultado:", a * b)
    elif op == "4":
        if b == 0:
            print("Divisão por zero!")
        else:
            print("Resultado:", a / b)
    elif op == "5":
        tabuada(a)
    else:
        print("Opção inválida.")
