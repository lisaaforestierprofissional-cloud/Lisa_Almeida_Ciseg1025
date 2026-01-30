from typing import List

ASCII_MIN = 32
ASCII_MAX = 126
ASCII_RANGE = ASCII_MAX - ASCII_MIN + 1


def calcular_chave_numerica(chave: str) -> int:
    if not chave:
        raise ValueError("A chave não pode ser vazia.")
    return sum(ord(c) for c in chave)


def rotacionar_ascii(valor: int) -> int:
    return ASCII_MIN + (valor - ASCII_MIN) % ASCII_RANGE


def criptografar(mensagem: str, chave: str) -> List[int]:
    chave_numerica = calcular_chave_numerica(chave)
    codigos = []

    for char in mensagem:
        valor = ord(char) + chave_numerica
        valor_rotacionado = rotacionar_ascii(valor)
        codigos.append(valor_rotacionado)

    return codigos


def descriptografar(codigos: List[int], chave: str) -> str:
    chave_numerica = calcular_chave_numerica(chave)
    mensagem = ""

    for codigo in codigos:
        valor = codigo - chave_numerica
        valor_rotacionado = rotacionar_ascii(valor)
        mensagem += chr(valor_rotacionado)

    return mensagem


def main():
    mensagem = input("Introduz a mensagem: ")
    chave = input("Introduz a chave: ")

    try:
        criptografada = criptografar(mensagem, chave)
        print("\nMensagem criptografada:")
        print(criptografada)

        descriptografada = descriptografar(criptografada, chave)
        print("\nMensagem descriptografada:")
        print(descriptografada)

    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
