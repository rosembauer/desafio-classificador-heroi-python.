# Lista de heróis para demonstrar o uso de variáveis, listas e dicionários
herois = [
    {"nome": "João", "xp": 800},
    {"nome": "Maria", "xp": 1500},
    {"nome": "Davi", "xp": 3500},
    {"nome": "Rhyan", "xp": 6500},
    {"nome": "Lua", "xp": 7500},
    {"nome": "Roberto", "xp": 8500},
    {"nome": "Paulo", "xp": 9500},
    {"nome": "Deus", "xp": 12000}
]

# Laço de repetição (for) para percorrer cada herói da lista
for heroi in herois:
    nome = heroi["nome"]
    xp = heroi["xp"]
    nivel = ""

    # Estrutura de decisão (if/elif/else) para determinar a patente com base no XP
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Saída formatada no terminal
    print(f"O Herói de nome {nome} está no nível de **{nivel}")
    