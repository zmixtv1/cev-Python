maior_quantidade = -1
maior_cnpj = ""
print("Digite [S] para finalizar")
while True:
    cnpj = input("Digite o Cnpj: ").upper()
    if cnpj == "S":
        break
    qtd = int(input("Digite a Quantidade de funcionários: "))
    if qtd > maior_quantidade:
        maior_quantidade = qtd
        maior_cnpj = cnpj