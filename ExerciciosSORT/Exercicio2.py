def ordenar_alfabetico_inverso(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            palavra1 = lista[j].lower()
            palavra2 = lista[j+1].lower()
            k = 0
            while k < len(palavra1) and k < len(palavra2):
                if ord(palavra1[k]) < ord(palavra2[k]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    break
                elif ord(palavra1[k]) > ord(palavra2[k]):
                    break
                k += 1
            if k == len(palavra2) and len(palavra1) > len(palavra2):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]
print(ordenar_alfabetico_inverso(palavras))
