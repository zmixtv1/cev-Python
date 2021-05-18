colocados = ("América-MG", "Athletico-PR",
             "Atlético-GO", "Atlético-MG", "Bahia",
             "Ceará sc", "Chapecoense", "Corinthias",
             "Cuiabá", "Flamengo", "Fluminense",
             "Fortaleza", "Gremio", "Internacional",
             "Juventude", "Palmeiras", "Bragantino",
             "Santos", "Sport Recife", "São Paulo")
print(f"Os 5 Primeiro colocados são {colocados[0:5]}")
print("-="*15)
print(f"OS ultimos 4 Colocados são {colocados[-4:]}")
print("-="*15)
print(f"Times em ordem alfabetica: {sorted(colocados)}")
print("-="*15)
print(f"o chapeconse está na {colocados.index('Chapecoense') + 1}ª posição")