lista = []
listapar = []
listaimpar = []
while True:
    num = int(input("Digite um valor: "))
    resp = str(input("Quer continuar[S/N]: ")).upper()
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    if resp == "N":
        break
print(f"A lista completa é: {lista}")
print(f"A lista de pares é: {listapar}")
print(f"A lista de ímpar é: {listaimpar}")
