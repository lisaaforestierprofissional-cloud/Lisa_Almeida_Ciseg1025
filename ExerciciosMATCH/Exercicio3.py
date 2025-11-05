operacao = {"tipo": "venda", "valor": 250}

if operacao["tipo"] == "compra":
    print(f"Compra de {operacao['valor']}€")
elif operacao["tipo"] == "venda":
    print(f"Venda de {operacao['valor']}€")
else:
    print("Pedido desconhecido")
