segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")
