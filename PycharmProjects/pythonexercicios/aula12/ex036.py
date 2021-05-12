valorCasa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o valor do salario da pessoa que vai comprar? R$"))
anos = int(input("Quantos anos vai ser o financiamento? "))
prestação = valorCasa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}".format(valorCasa, anos, prestação))

if prestação <= minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Emprestimo NEGADO!")