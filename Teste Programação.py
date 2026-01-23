import datetime

titulos = []
diretores = []
anos = []
generos = []

MAX = 100


def adicionar_filme():
    if len(titulos) == MAX:
        print("Não é possível adicionar mais filmes.")
        return

    titulo = input("Título: ")
    diretor = input("Diretor: ")

    for i in range(len(titulos)):
        if titulos[i] == titulo and diretores[i] == diretor:
            print("Filme já existe.")
            return

    try:
        ano = int(input("Ano de lançamento: "))
        ano_atual = datetime.datetime.now().year
        if ano < 1888 or ano > ano_atual:
            print("Ano inválido.")
            return
    except:
        print("Erro no ano.")
        return

    genero = input("Gênero: ")

    titulos.append(titulo)
    diretores.append(diretor)
    anos.append(ano)
    generos.append(genero)

    print("Filme adicionado.")


def procurar_filme():
    print("1 - Título")
    print("2 - Diretor")
    print("3 - Gênero")
    op = input("Opção: ")

    termo = input("Procurar: ")
    encontrado = False

    for i in range(len(titulos)):
        if (op == "1" and titulos[i] == termo) or \
           (op == "2" and diretores[i] == termo) or \
           (op == "3" and generos[i] == termo):
            print(i, titulos[i], diretores[i], anos[i], generos[i])
            encontrado = True

    if not encontrado:
        print("Nenhum filme encontrado.")


def excluir_filme():
    try:
        pos = int(input("Posição do filme: "))
        print(titulos[pos], "-", diretores[pos])
        conf = input("Confirmar exclusão? (s/n): ")

        if conf == "s":
            titulos.pop(pos)
            diretores.pop(pos)
            anos.pop(pos)
            generos.pop(pos)
            print("Filme removido.")
        else:
            print("Operação cancelada.")
    except IndexError:
        print("Índice inválido.")
    except:
        print("Erro na entrada.")


def ordenar_filmes():
    print("1 - Título")
    print("2 - Diretor")
    print("3 - Ano")
    op = input("Opção: ")

    for i in range(len(titulos)):
        for j in range(i + 1, len(titulos)):
            if (op == "1" and titulos[i] > titulos[j]) or \
               (op == "2" and diretores[i] > diretores[j]) or \
               (op == "3" and anos[i] > anos[j]):
                titulos[i], titulos[j] = titulos[j], titulos[i]
                diretores[i], diretores[j] = diretores[j], diretores[i]
                anos[i], anos[j] = anos[j], anos[i]
                generos[i], generos[j] = generos[j], generos[i]

    print("Filmes ordenados.")


def listar_filmes():
    if len(titulos) == 0:
        print("Não existem filmes cadastrados.")
    else:
        for i in range(len(titulos)):
            print(i, titulos[i], diretores[i], anos[i], generos[i])


def menu():
    while True:
        print("\nMENU")
        print("1 - Adicionar filme")
        print("2 - Procurar filme")
        print("3 - Excluir filme")
        print("4 - Ordenar filmes")
        print("5 - Listar filmes")
        print("6 - Sair")

        op = input("Opção: ")

        if op == "1":
            adicionar_filme()
        elif op == "2":
            procurar_filme()
        elif op == "3":
            excluir_filme()
        elif op == "4":
            ordenar_filmes()
        elif op == "5":
            listar_filmes()
        elif op == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


menu()
