nome = input("Introduza o seu nome completo: ")

palavra = ""
i = 0

while i < len(nome):
    c = nome[i]

    if c == ' ':
        if palavra != "":
            if palavra not in ["de", "da", "do", "dos", "das"]:
                if palavra[0] != palavra[0].upper():
                    print("Nome inválido: contém caracteres não permitidos.")
                    break
            palavra = ""
        i += 1
        continue

    if not c.isalpha():
        print("Nome inválido: contém caracteres não permitidos.")
        break

    palavra += c
    i += 1
else:
    if palavra not in ["de", "da", "do", "dos", "das"]:
        if palavra[0] != palavra[0].upper():
            print("Nome inválido: contém caracteres não permitidos.")
    else:
        print("Nome válido!")
        exit()

    print("Nome válido!")


