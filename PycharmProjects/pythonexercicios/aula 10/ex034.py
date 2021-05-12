salario = float(input('Qual o valor do salario atual: R$'))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
    print('O valor do seu salario é de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 10/100)
    print('O valor do seu salario é de R${:.2f}'.format(aumento))