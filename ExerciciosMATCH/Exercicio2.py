classificacao = input("Digite a classificação (Excelente, Bom, Suficiente, Insuficiente): ").strip().capitalize()


if classificacao == "Excelente":
    print("90-100")
elif classificacao == "Bom":
    print("70-89")
elif classificacao == "Suficiente":
    print("50-69")
elif classificacao == "Insuficiente":
    print("0-49")
else:
    print("Classificação inválida!")
