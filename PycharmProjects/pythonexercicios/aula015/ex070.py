maisDeMil = menor = total = cont = 0
barato = ""
while True:
    nome = str(input("Digite o nome do produto: "))
    preço = int(input("Digite o valor do produto: R$"))
    cont += 1
    total += preço
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if preço > preço:
        barato = nome
    if preço > 1000:
        maisDeMil += 1
    if resp == "N":
        break
print("Acabou")
print(f"O total da compra foi {total}")
print(f"{maisDeMil} produtos custam mais de mil")
print(f"O nome do produto mais barato é {barato} e custa R${menor:.2f}")
