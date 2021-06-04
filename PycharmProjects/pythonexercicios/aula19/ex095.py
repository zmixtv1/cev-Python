time = list()
jogador  = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na {c+1}° partida? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("'Erro' Responda apenas S ou N.")
    if resp == "N":
        break
print("_" * 40)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("_" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15} ", end="")
    print()
print("-"*40)

while True:
    busca = int(input("mostrar dados de qual jogador? (999 Para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro ! Não existe jogador com código {busca}!")
    else:
        print(f"-- levantamento Do Jogador {time[busca]['nome']} --")
        for i, g in enumerate(time[busca]['gols']):
            print(f"     No jogo {i + 1} fez {g} gols. ")
    print("_"*40)
print("<< Volte Sempre >>")
