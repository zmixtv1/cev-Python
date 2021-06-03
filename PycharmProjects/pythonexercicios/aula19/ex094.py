lista = list()
dados = dict()
soma = media = 0
mulher = list()
while True:
    dados.clear()
    dados["Nome"] = str(input("Nome: ")).capitalize()
    while True:
        dados["Sexo"] = str(input("Sexo[M/F]: ")).upper()[0]
        if dados["Sexo"] in "MF":
            break
        print("Erro! Por favor, digite apenas M ou F.")
    if dados["Sexo"] in "F":
        mulher.append(dados["Nome"])
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    lista.append(dados.copy())
    cont = str(input("Quer continuar[S/N]: ")).upper()[0]
    if cont != "S":
        break
print("-=" * 30)
print(f"O grupo tem {len(lista)} pessoas.")
media = soma / len(lista)
print(f"A média de idade é de {media:.2f} anos. ")

print(f"As mulheres cadastradas foram: ", end=" ")
for k in mulher:
    print(f"{k}", end=" ")

print()
print("Lista das pessoas acima da media:")
for p in lista:
    if p["idade"] >= media:
        print("         ")
        for k, v  in p.items():
            print(f"{k} = {v}; ", end="")
        print()

print("<<ENCERRADO>>")
