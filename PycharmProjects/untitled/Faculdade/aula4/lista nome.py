nome = str(input('Digite um nome: '))
for letra in nome:
    print(letra)

print('_' * 10)
nun = 1
for abc in nome:
    print(nun * abc)
    nun += 1

print('_' * 10)

nun = 1
for acd in nome:
    print(nome[0:nun])
    nun += 1
