'''teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
print(galera[0][0],galera[1][1])'''

galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1
print(f"temos {totmai} maiores e {totmen} menores de idade.")
