frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas letras a aparece na frase?: {}'.format(frase.count('A')))
print('A primeira letra apareceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A aparecer na posição {}'.format(frase.rfind('A') + 1))