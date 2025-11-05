operacao = input("Digite a operação (soma, subtrai, multiplica, divide): ").strip().lower()
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))


if operacao == "soma":
    resultado = num1 + num2
elif operacao == "subtrai":
    resultado = num1 - num2
elif operacao == "multiplica":
    resultado = num1 * num2
elif operacao == "divide":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print(resultado)
