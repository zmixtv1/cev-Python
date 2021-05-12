velho = 0
menos = 0
for c in range(1, 5):
    print("-------- {}ª PESSOA ---------".format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]:  ").upper())
    if c == 1:
        velho = idade
    else:
        if idade > velho:
            velho = idade
    if c == 1:
        if sexo == "F":
            menos = idade
        else:
            if idade > menos:
                menos = idade