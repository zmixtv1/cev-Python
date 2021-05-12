nota1 = -1
while nota1 < 0 or nota1 > 10:
    nota1 = float(input('primeira nota: '))

nota2 = -1
while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Segunda nota: '))
nota3 = -1
while nota3 < 0 or nota3 > 10:
    nota3 = float(input('Terceira nota: '))

media = ((nota1*1) + (nota2*1.5) + (nota3*2)) / 4.5
print('A média é: {:.2f}'.format(media))

if media == 0:
    print('SR')
elif media <2:
    print('II')
elif media <5:
    print('MI')
elif media <7:
    print('MM')
elif media <9:
    print('MS')
else:
    print('SS')
