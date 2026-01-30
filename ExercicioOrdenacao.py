def ordenar_nomes(lista_nomes: list) -> list:
    return sorted(
        lista_nomes,
        key=lambda nome: (
            nome.split()[0],  # primeiro nome
            nome.split()[1]   # apelido
        )
    )


def main():
    nomes = [
        "Pedro Pereira",
        "Ana Beatriz",
        "Ana Clara",
        "Carlos Silva",
        "Beatriz Souza",
        "Ana Paula",
        "Pedro Andrade"
    ]

    nomes_ordenados = ordenar_nomes(nomes)

    print("Nomes ordenados:")
    for nome in nomes_ordenados:
        print(nome)


if __name__ == "__main__":
    main()
