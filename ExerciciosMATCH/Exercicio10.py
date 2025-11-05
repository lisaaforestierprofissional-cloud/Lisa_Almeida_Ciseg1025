requisicao = {"metodo": "POST", "conteudo": ""}

metodo = requisicao.get("metodo", "").upper()
conteudo = requisicao.get("conteudo", "")


if metodo == "GET":
    resultado = "Requisição GET recebida"
elif metodo == "POST" and conteudo:
    resultado = "Requisição POST com dados válidos"
elif metodo == "POST" and not conteudo:
    resultado = "Requisição POST sem dados"
else:
    resultado = "Método não suportado"

print(resultado)
