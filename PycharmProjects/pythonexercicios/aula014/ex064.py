n1 = int(input("digite um valor: [999 para parar] "))
cont = 0
soma = n1
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input("Digite um valor: "))
print("Você digitou {} numeros e a soma entre eles foi de {}!".format(cont, soma))
