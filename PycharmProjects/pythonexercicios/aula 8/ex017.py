from math import hypot
co = float(input('Me fale o valor do cateto oposto:'))
ca = float(input('Me fale o valor do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))
