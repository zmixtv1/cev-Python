núm = (int(input("Digite um valor: ")),
        int(input("Digite outro valor: ")),
        int(input("Digite mais um valor: ")),
        int(input("Digite o ultimo valor: ")))
print(f"Você digitou os valores {núm}")
print(f"Você digitou o numero 9: {núm.count(9)} veze")
if 3 in núm:
    print(f"o valor 3 apareceu na {núm.index(3) + 1}ª posição")
else:
    print(f"você não digitou o valor 3 !")
print(f"Os valores pares digitados foram: ", end="")
for n in núm:
    if n % 2 == 0:
        print(n, end=" -> ")
print("Fim")