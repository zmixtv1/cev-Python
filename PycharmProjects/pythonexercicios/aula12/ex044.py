valor = float(input("Qual o valor do produto: "))
print("Escolha a forma de pagamento")
print("[ 1 ] À vista dinheiro/cheque")
print("[ 2 ] À vista no Cartão")
print("[ 3 ] em até 2x no Cartão")
print("[ 4 ] 3x ou mais no Cartão")
opção = int(input("Qual opção você escolheu? "))

disc1 = valor - (10 / 100)
disc2 = valor - (5 / 100)
disc3 = valor
disc4 = valor + (120 / 100)

if opção == 1:
    print("você recebeu 10% de desconto")
    print(disc1)
elif opção == 2:
    print("você recebeu 5% de desconto")
    print(disc2)
elif opção == 3:
    print("Preço normal")
    print(disc3)
elif opção == 4:
    print("você tera que pagar 20% de juros ")
    print(disc4)
