menor =99999999
valor = -1
qnt = 0
while True:
    if valor == 0:
        break
    else:
        valor = int(input("Digite um valor inteiro [0]SAIR: "))
        if valor != 0:
            if menor >= valor:
                menor = valor
                qnt += 1

print(f"O menor valor digitado foi {menor}, a quantidade de valores digitados é {qnt}")