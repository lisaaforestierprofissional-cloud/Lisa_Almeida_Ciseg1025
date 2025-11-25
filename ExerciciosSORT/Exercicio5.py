def agrupar_por_inicial(lista):
    grupos = {}
    for palavra in lista:
        inicial = palavra[0].lower()
        if inicial not in grupos:
            grupos[inicial] = []
        grupos[inicial].append(palavra)
    for inicial in grupos:
        n = len(grupos[inicial])
        for i in range(n):
            for j in range(0, n-i-1):
                palavra1 = grupos[inicial][j]
                palavra2 = grupos[inicial][j+1]
                k = 0
                while k < len(palavra1) and k < len(palavra2):
                    if ord(palavra1[k]) > ord(palavra2[k]):
                        grupos[inicial][j], grupos[inicial][j+1] = grupos[inicial][j+1], grupos[inicial][j]
                        break
                    elif ord(palavra1[k]) < ord(palavra2[k]):
                        break
                    k += 1
                if k == len(palavra2) and len(palavra1) > len(palavra2):
                    grupos[inicial][j], grupos[inicial][j+1] = grupos[inicial][j+1], grupos[inicial][j]
    return grupos

palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
print(agrupar_por_inicial(palavras))
