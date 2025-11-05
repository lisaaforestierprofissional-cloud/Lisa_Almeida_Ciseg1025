dias_uteis = ["segunda", "terça", "quarta", "quinta", "sexta"]
fim_de_semana = ["sábado", "domingo"]


dia = input("Digite o nome do dia da semana: ").strip().lower()


if dia in dias_uteis:
    print("Dia útil")
elif dia in fim_de_semana:
    print("Fim de semana")
else:
    print("Dia inválido! Digite um nome válido de dia da semana.")
