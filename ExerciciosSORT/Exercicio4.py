def contar_minusculas(palavra):
    count = 0
    for c in palavra:
        if 'a' <= c <= 'z':
            count += 1
    return count

def ordenar_por_minusculas(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if contar_minusculas(lista[j]) > contar_minusculas(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
print(ordenar_por_minusculas(palavras))
