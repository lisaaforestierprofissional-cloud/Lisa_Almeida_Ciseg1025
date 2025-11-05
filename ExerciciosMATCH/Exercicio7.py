servidor = {"status": "ok", "tempo_resposta": 350}


if servidor.get("status") == "ok" and servidor.get("tempo_resposta", 0) > 200:
    estado = "Servidor lento"
elif servidor.get("status") == "ok":
    estado = "Servidor ativo"
elif servidor.get("status") == "erro":
    estado = "Servidor indisponível"
else:
    estado = "Estado desconhecido"


print(estado)
