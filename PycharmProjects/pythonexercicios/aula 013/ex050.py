soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("digite o {}° valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("você informou {} numeros pares e a soma foi {}!".format(cont, soma))
