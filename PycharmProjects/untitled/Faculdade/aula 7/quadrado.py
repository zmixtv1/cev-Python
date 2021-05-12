'''lado = int(input("Quantos caracteres no lado do quadrado [10-100]? "))
if lado < 10 or lado > 100:
   print ("Informe um número entre 1 e 100!")
else:
   for linha in range(0, lado):
       print()
       for coluna in range(0, lado):
           if linha == 0 or coluna == 0 or linha == (lado-1) or coluna == (lado-1):
               print(" + ", end="")
           elif linha == coluna:
               print(" + ", end="")
           elif linha + coluna == lado - 1:
               print(" + ", end="")
           else:
               print(" 0 ", end="")

'''
'''
lado = str(input("Digite um nome? "))
lado = len(lado)
for linha in range(0, lado):
    print()
    for coluna in range(0, lado):
        if linha == 0 or coluna == 0 or linha == (lado-1) or coluna == (lado-1):
            print(" + ", end="")
        elif linha == coluna:
            print(" + ", end="")
        elif linha + coluna == lado - 1:
            print(" + ", end="")
        else:
            print(" 0 ", end="")
'''
'''
nome = str(input("Digite um nome: "))
for c in nome:
    print(nome, end=" -> ")
print("Fim")
'''

nome = ""
while len(nome) < 3:
    nome = input(str('Digita nome: '))
    if len(nome) < 3:
        print("Digiteum nome valido")
    else:
        print(nome)
