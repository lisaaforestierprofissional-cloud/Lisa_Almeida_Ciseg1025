for i in range(0, 256):
    print(i, chr(i))
    if i % 20 == 0 and i != 0:
        opc = input("Continuar? (s/n) ")
        if opc.lower() != "s":
            break
