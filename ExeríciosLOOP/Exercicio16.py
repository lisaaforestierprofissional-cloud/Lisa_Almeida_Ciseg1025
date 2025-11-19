soma = 0
count = 0

while count < 30:
    n = int(input("Digite um número par entre 1 e 50: "))
    if n % 2 == 0 and 1 <= n <= 50:
        soma += n
        count += 1

media = soma / 30
print("Média:", media)
