'''
m = 1
for a in range(97, 122):
    for m in range(96, a):
        print(chr(a), end="")
    print()
'''

'''
numRep=1
for num in range(49, 58):
   for repete in range(0, numRep):
       print(chr(num), end="")
   print()
   numRep+=1
'''

print("A seguir iremos aplicar a Cifra de César sobre um texto com deslocamento de 2 casas")
print("Informe uma frase:")
frase = input()
if (len(frase)==0):
   print ("Informe uma frase por favor")
else:
   cesar=""
   for ind in range(0, len(frase)):
       codigo=ord(frase[ind])
       codigo += 2
       novoCaracter=chr(codigo)
       cesar+=novoCaracter

   print("A frase cifrada é")
   print(cesar)

'''
print()
for a in range(97, 123):
    for rep in range(10):
        print(chr(a),end='')
    print()

for a in range (97, 123):
    print(chr(a))
'''

print("Informe uma frase")
frase = input()
if (len(frase)==0):
    print("Informe Uma frase por favor")
else:
    a = ""
    for num in range(0, len(frase)):
        cod=ord(frase[num])
        cod -= 2
        nc = chr(cod)
        a += nc
    print("A frase descriptografada é:")
    print(a)