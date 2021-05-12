frase = str(input('Escreva uma frase: '))
print(frase.upper().replace('E', 'and'))
print(frase.lower().replace('e', 'and'))
print(frase.replace('e', 'and'))

frase2 = str(input('Escreva uma frase: '))
print(frase2.strip().replace(' ', ''))


frase3 = str(input('Escreva uma frase:'))
m1 = frase3.capitalize().replace(' ', '').strip()
print("A frase '{}' contem apenas letras: {}".format(frase3, m1.isalpha()))
print("Na frase '{}' existe a palavra 'apenas'?: {}".format(frase3, 'apenas' in frase3))
