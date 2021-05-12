prod = float(input('Qual é o valor do produto:'))
preço = prod - (prod*5/100)
print('O valor do produto na promoção é de R${:.2f}'.format(preço))
