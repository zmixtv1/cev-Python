km = float(input('Qual a distancia em km: '))
if km <= 200:
    valor1 = km * 0.5
    print('o valor da passagem é de R${:.2f}'.format(valor1))

else:
    valor2 = km * 0.45
    print('O valor da passagem é de R${:.2f}'.format(valor2))
