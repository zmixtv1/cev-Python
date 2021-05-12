v1 = int(input("Digite um valor: "))
v2 = int (input("Digite outro valor: "))

if v1 > v2:
    print("O valor {} é maior que o {}".format(v1, v2))
elif v1 < v2:
    print("O valor {} é maior que o valor {}".format(v2, v1))
else:
    print("Não existe valor maior, os dois são iguais")
