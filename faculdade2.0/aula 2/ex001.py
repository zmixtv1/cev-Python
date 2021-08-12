lista = []
print("Digite [0] para sair")
while True:
    valor = int(input("valor: "))
    if valor == 0:
        break
    lista.append(valor)

print(f"quantidade de elementos na lista {len(lista)}")
print(f"Soma: {sum(lista)}")
print(f"maior vetor: {max(lista)}")
print(f"menor valor: {min(lista)}")
pesquisa = int(input("Valor da pesquisa: "))
if pesquisa in lista:
    print("valor encontrado.")
else:
    print("valor não encontrado")
lista.sort()
print(f"lista na ordem crescente: {lista}")
lista.insert(1,33)
print(lista)
lista.sort(reverse=True)
print(f"Decrescente:{lista}")
print(f"média: {sum(lista)/len(lista)}")


ct = 0
for v in lista:
    if v > 10:
        ct+=1
porc = ct / len(lista) * 100
print(f"Porcentagem de numeros maiores que 10: {porc}")

l_maior_10 = []
for v in lista:
    if v > 10:
        l_maior_10.append(v)
porc = len(l_maior_10)