'''
def ficha(nome, gols):
    if nome == "":
        nome = "<desconhecido>"
    if gols == "":
        gols = 0
    print(f"o jogador {nome} fez {gols} gols no campeonato")


nome = str(input("Nome do Jogador: "))
gols = input("Quantos gols ele marcou: ")
ficha(nome, gols)
'''


def ficha(jog="<desconhecido>", gols=0):
    print(f"o jogador {jog} fez {gols} gol(s) no campeonato.")


n = str(input("Nome do jogador: "))
g = str(input("número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gols=g)
else:
    ficha(n,g)