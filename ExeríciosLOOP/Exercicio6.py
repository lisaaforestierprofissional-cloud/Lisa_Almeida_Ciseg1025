def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador = 0
num = 2

while contador < 10:
    if eh_primo(num):
        print(num)
        contador += 1
    num += 1
