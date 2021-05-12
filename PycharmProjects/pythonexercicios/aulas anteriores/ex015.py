dias = int(input('Quanto dias alugados? '))
km = float(input('Quantos kM rodados? '))
vd = dias * 60
vkm = km * 0.15
vt = vd + vkm
print('o total de pagar pelo aluguel é de R${:.2f}'.format(vt))
