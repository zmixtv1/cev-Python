n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.2f}'.format(m))
if m >= 6:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('A sua média foi ruim!! ESTUDE MAIS!!')
print('Fim')