clientes = []
numcli_auto = 1


def calcular_desconto(valor):
    if 100 <= valor <= 200:
        return valor * 0.05
    elif 200 < valor <= 500:
        return valor * 0.10
    elif valor > 500:
        return valor * 0.15
    return 0.0


def ler_float(prompt):
    while True:
        try:
            v = float(input(prompt))
            return v
        except ValueError:
            print("Valor inválido. Tente novamente.")


def ler_int(prompt):
    while True:
        try:
            v = int(input(prompt))
            return v
        except ValueError:
            print("Valor inválido. Tente novamente.")


while True:
    print("""
------- MENU CLIENTES -------
1 - Inserir cliente
2 - Listar clientes
3 - Procurar cliente por número
0 - Sair
""")

    opc = input("Opção: ").strip()

    if opc == "0":
        print("Saindo...")
        break

    elif opc == "1":
        nome = input("Nome: ").strip()
        morada = input("Morada: ").strip()
        tel = input("Telefone: ").strip()
        nif = input("NIF: ").strip()

        while True:
            compra = ler_float("Valor da compra (>= 0): ")
            if compra >= 0:
                break
            print("O valor da compra deve ser >= 0.")

        desconto = calcular_desconto(compra)
        divfin = compra - desconto

        cliente = {
            "Numero": numcli_auto,
            "Nome": nome,
            "Morada": morada,
            "Telefone": tel,
            "NIF": nif,
            "Compra": compra,
            "Desconto": desconto,
            "DivFinal": divfin
        }

        clientes.append(cliente)
        print(f"Cliente registado com sucesso! Número do cliente: {numcli_auto}")
        numcli_auto += 1

    elif opc == "2":
        if not clientes:
            print("Não há clientes registados.")
            continue

        for c in clientes:
            print("\n--- Cliente", c["Numero"], "---")
            print("Nome:", c["Nome"])
            print("Morada:", c["Morada"])
            print("Telefone:", c["Telefone"])
            print("NIF:", c["NIF"])
            print("Compra:", c["Compra"])
            print("Desconto:", c["Desconto"])
            print("Dívida Final:", c["DivFinal"])

            continuar = input("Próximo cliente? (s/n): ").strip().lower()
            if continuar != "s":
                break

    elif opc == "3":
        if not clientes:
            print("Não há clientes registados.")
            continue

        procura = ler_int("Número do cliente: ")
        encontrado = False

        for c in clientes:
            if c["Numero"] == procura:
                encontrado = True
                print("\n--- Cliente encontrado ---")
                print("Número:", c["Numero"])
                print("Nome:", c["Nome"])
                print("Morada:", c["Morada"])
                print("Telefone:", c["Telefone"])
                print("NIF:", c["NIF"])
                print("Compra:", c["Compra"])
                print("Desconto:", c["Desconto"])
                print("Dívida Final:", c["DivFinal"])
                break

        if not encontrado:
            print("Cliente não existe.")

    else:
        print("Opção inválida!")
