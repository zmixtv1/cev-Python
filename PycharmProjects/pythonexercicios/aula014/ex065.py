n1 = int(input("Digite um numero: "))
continuar = str(input("Quer continuar? [S/N] ")).upper().strip()
maior = menor = n1
quant = total = 0
while continuar != "N":
    n1 =int(input("Digite um numero: "))
    if maior < n1:
        maior = n1
    elif menor > n1:
        menor = n1
    total += n1
    quant += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()
media = total / quant
print("A media entre todo os valores digitados é {:.2f} e o maior numero é {} e o menor {}".format(media, maior, menor))
