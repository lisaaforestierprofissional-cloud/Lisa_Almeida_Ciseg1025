# input() le o que escrevemos no terminal

nome=""
altura=0.0   # tipo float numeros co virgula (.)
num1=0

print("Introduza o seu nome")
nome=input()

print(type(nome))

        # float <---- string        casting
altura=float(input("Introduza a sua altura"))

print(type(altura))

        # int <---- string        casting
num1=int(input("Introduza um numero"))

print(type(num1), end="\n\n")



print(f"Este e o seu nome : {nome} ")
print(f"Este e a sua altura : {altura} ")
print(f"Este o seu numero : {num1} ")

print(f"Este e o seu nome: {nome}, altura: {altura}, numero: {num1}")
