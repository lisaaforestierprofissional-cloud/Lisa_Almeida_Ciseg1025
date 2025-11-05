tipo = input("Digite um tipo (inteiro, decimal, string numérica, string textual, lista): ").strip().lower()


if tipo == "inteiro":
    valor = 42
elif tipo == "decimal":
    valor = 3.14
elif tipo == "string numérica":
    valor = "123"
elif tipo == "string textual":
    valor = "Olá, mundo!"
elif tipo == "lista":
    valor = [10, 20, 30]
else:
    valor = "Tipo desconhecido"

print(valor)
