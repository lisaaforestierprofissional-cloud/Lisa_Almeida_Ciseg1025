mensagem = input("Digite uma mensagem: ").strip().lower()


if mensagem in ["olá", "bom dia"]:
    tipo = "Saudação"
elif mensagem.endswith("?"):
    tipo = "Pergunta"
elif "tchau" in mensagem or "adeus" in mensagem:
    tipo = "Despedida"
else:
    tipo = "Mensagem genérica"


print(tipo)
