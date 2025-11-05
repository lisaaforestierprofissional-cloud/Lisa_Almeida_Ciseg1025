usuario = {"nome": "João", "idade": 30, "tipo": "admin"}

idade = usuario.get("idade", 0)
tipo = usuario.get("tipo", "").lower()

if idade < 18:
    classificacao = "Utilizador menor de idade"
elif tipo == "admin":
    classificacao = "Administrador"
else:
    classificacao = "Utilizador comum"

print(classificacao)
