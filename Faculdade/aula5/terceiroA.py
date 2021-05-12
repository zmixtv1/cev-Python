frase = str(input('Digite uma palavra:'))

nf = ''

for i in range(0, int(len(frase)/2)):
    nf += frase[int(len(frase)) -1 -i]
    nf += frase[i]
if len(frase) % 2 != 0:
    nf += frase[int(len(frase)/2)]

print(nf)
