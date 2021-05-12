peso = float(input("Digite seu peso: "))
altura = float(input("Digite sia altura: "))

imc = peso / (altura ** 2)

print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc <= 18.5:
    print("Abaixo do peso!")
elif imc > 18.5 and imc <= 25:
    print("Peso ideal")
elif imc > 25 and imc <= 30:
    print("Sobrepeso")
else:
    print("obesidade mórbida")
    