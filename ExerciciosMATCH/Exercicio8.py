produto = {"categoria": "eletrônico", "preco": 1500}

categoria = produto.get("categoria", "").lower()
preco = produto.get("preco", 0)

if categoria == "eletrônico" and preco > 1000:
    classificacao = "Produto de luxo"
elif categoria == "eletrônico" and preco <= 1000:
    classificacao = "Produto comum"
elif categoria == "alimento":
    classificacao = "Produto alimentar"
else:
    classificacao = "Categoria desconhecida"


print(classificacao)
