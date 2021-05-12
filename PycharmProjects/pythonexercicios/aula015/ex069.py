maior = homem = mulher = 0
while True:
    print("-" * 30)
    print("Vamos cadastrar uma pessoa!")
    print("-" * 30)
    idade = int(input("idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo= str(input("sexo [M/F]: ")).strip().upper()
    resp = " "
    if sexo in "M":
        homem += 1
    if idade >= 18:
        maior += 1
    if idade > 20 and sexo in "F":
        mulher += 1
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == "N":
        break
print("-" * 30)
print(f"total de pessoas maior de 18 anos={maior}\nTotal de homens:{homem}\nTotal de Mulher abaixo de 20 anos:{mulher}")
print("Acabou")
