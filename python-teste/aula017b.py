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
for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

print(galera)