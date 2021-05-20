import random
print('''Suas  opções
[ 0 ] coroa
[ 1 ] cara ''')
jogador = int(input("Qual é a sua jogada?  "))

class CaraCoroa:
    def __init__(self):
        self.lado = 'Cara'

    def lancar(self):
        if (random.randint(0, 1)) % 2 == 0:
            self.lado = 'Cara'
        else:
            self.lado = 'Coroa'
        return self.lado


moeda = CaraCoroa()
op = 1

if 
while op:
    if op:
        print(moeda.lancar())

    op = int(input("0.Sair\n"
                   "1.Jogar de novo\n"))
