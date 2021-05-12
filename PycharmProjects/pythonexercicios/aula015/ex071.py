print("=" * 30)
print("            Banco           ")
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$"))
nota50 = nota20 = nota10 = nota1 = 0
while valor != 0:
    if valor >= 50:
        while valor >= 50:
            valor -= 50
            nota50 += 1
    elif valor >= 20:
        while valor >= 20:
            valor -= 20
            nota20 += 1
    elif valor >= 10:
        while valor >= 10:
            valor -= 10
            nota10 += 1
    elif valor >= 1:
        while valor >= 1:
            valor -= 1
            nota1 += 1
print(f"Total de {nota50} cédulas de R$50,00\nTotal de {nota20} cédulas de R$20,00\nTotal de {nota10} cédulas de R$10,00\nTotal de {nota1} Cédulas de R$1,00")
