import re
from datetime import datetime

# Nome da pasta para o Python não se perder
pasta = "Exercicios regex txt/"

try:
    with open(pasta + 'registos.txt', 'r', encoding='utf-8') as f:
        texto_completo = f.read()

    # Exercícios 7 a 10: Extração com Regex
    nifs = re.findall(r'NIF:\s*(\d{9})', texto_completo)
    datas = re.findall(r'\d{2}/\d{2}/\d{4}', texto_completo)
    codigos_postais = re.findall(r'\d{4}-\d{3}', texto_completo)
    dominios = re.findall(r'https?://(?:www\.)?([a-z0-9.-]+)', texto_completo)
    nomes = re.findall(r'Nome:\s*(.*?)\s*\|', texto_completo)

    # Exercício 11: Validar NIFs
    nifs_validos = [n for n in nifs if n[0] in "123568"]
    print(f"NIFs válidos: {nifs_validos}")

    # Exercício 12: Criar ficheiro resumo
    with open(pasta + 'resumo.txt', 'w', encoding='utf-8') as f_res:
        for i in range(len(nomes)):
            linha = f"{nomes[i]} | {nifs[i]} | {datas[i]} | {codigos_postais[i]} | {dominios[i]}\n"
            f_res.write(linha)

    # Exercício 13: Datas anteriores a 2025
    print("\nRegistos anteriores a 2025:")
    for d_str in datas:
        if datetime.strptime(d_str, "%d/%m/%Y").year < 2025:
            print(f"- {d_str}")

    print("\nSucesso! Verifica o ficheiro resumo.txt na tua pasta.")

except FileNotFoundError:
    print("Erro: Confirma se os ficheiros .txt estão na pasta correta!")