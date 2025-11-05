jogador1 = input("Jogador 1: ").strip().lower()
jogador2 = input("Jogador 2: ").strip().lower()


match (jogador1, jogador2):
    case (a, b) if a == b:
        resultado = "Empate"
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        resultado = "Jogador 1 venceu"
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        resultado = "Jogador 2 venceu"
    case _:
        resultado = "Jogada inválida"

print(resultado)
