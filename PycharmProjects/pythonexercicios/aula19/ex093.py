gols = list()
tot = 0
nome = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {nome} Jogou: "))
for c in range(0, partidas):
    gol = int(input(f"Quantos Gols na {c+1}º partida: "))
    gols.append(gol)
    tot += gol
dados = {"Nome": nome, "gols": gols, "Total": tot}
print("-=" * 30)
print(dados)
print("-=" * 30)
for k, v in dados.items():
    print(f"O camppo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {nome} jogou {partidas} partidas.")
for c, v in enumerate(gols):
    print(f"   => Na {c+1}° Partida, Fez {v} gols.")
print(f"Foi um total de {tot} Gols.")
