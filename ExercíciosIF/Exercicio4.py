saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque > saldo:
    print("Cheque não pode ser descontado. Saldo insuficiente.")
else:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo}")
