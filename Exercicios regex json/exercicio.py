import json
import re

pasta = 'Exercicios regex json/'

# --- Exercício 1: Ler o ficheiro JSON ---
def ler_dados():
    try:
        # Ajustado para procurar dentro da pasta correta
        with open(pasta + 'dados.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Ficheiro dados.json não encontrado em: {pasta}")
        return []

dados = ler_dados()

# --- Exercício 2: Validar emails com regex ---
regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validar_email(email):
    return bool(re.match(regex_email, email))

# --- Exercício 3: Extrair domínios dos sites ---
def extrair_dominio(url):
    dominio = re.sub(r'https?://(www\.)?', '', url).split('/')[0]
    return dominio

print("Domínios extraídos:")
for pessoa in dados:
    print(f"- {extrair_dominio(pessoa['site'])}")

# --- Exercício 4: Validar NIFs com regex ---
regex_nif = r'^[123568]\d{8}$'

def validar_nif(nif):
    return bool(re.match(regex_nif, nif))

# --- Exercício 5: Guardar registos válidos ---
def validar_telemovel(tel):
    apenas_numeros = re.sub(r'\D', '', tel)
    return len(apenas_numeros) == 9

registos_validos = []

for pessoa in dados:
    if (validar_email(pessoa['email']) and 
        validar_nif(pessoa['nif']) and 
        validar_telemovel(pessoa['telemovel'])):
        registos_validos.append(pessoa)

# Guardar o ficheiro validos.json dentro da pasta
with open(pasta + 'validos.json', 'w', encoding='utf-8') as f:
    json.dump(registos_validos, f, indent=4, ensure_ascii=False)

print(f"\n{len(registos_validos)} registos válidos guardados em '{pasta}validos.json'.")

# --- Exercício 6: Criar ficheiro .txt com nome e email ---
with open(pasta + 'lista_contactos.txt', 'w', encoding='utf-8') as f:
    for pessoa in dados:
        linha = f"Nome: {pessoa['nome']} | Email: {pessoa['email']}\n"
        f.write(linha)

print(f"Ficheiro '{pasta}lista_contactos.txt' criado com sucesso.")