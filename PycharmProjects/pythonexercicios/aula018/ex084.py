lista = list()
dados = list()
mai = men = 0

while True:
    dados.append(str(input("Nome: ").capitalize()))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input("Quer continuar[S/N]: ")).upper()
    if resp == "N":
        break
print("-=" * 30)
print(f"Total de pessoas cadastradas {len(lista)}")
print(f"o maior peso foi de {mai}kg ", end="")
for p in lista:
    if p[1] == mai:
        print(f"[{p[0]}]",end="")
print()
print(f"o menor peso foi de {men}kg ", end="")
for p in lista:
    if p[1] == men:
        print(f"[{p[0]}]",end="")