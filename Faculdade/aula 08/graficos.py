'''
from graphics import *
import random
import time
numero_janelas = random.randrange(10, 1000)
for i in range(numero_janelas):
   largura = random.randrange(300, 1300)
   altura = random.randrange(300, 500)
   vermelho = random.randrange(0, 256)
   verde = random.randrange(0, 256)
   azul = random.randrange(0, 256)

   jan = GraphWin("Janela-" + str(i), largura, altura)
   jan.setBackground(color_rgb(vermelho, verde, azul))
   time.sleep(.2)
jan.getMouse()
jan.close()

from graphics import *

janela = GraphWin("Pontos ...", 900, 500)

# Desenhando pontos método-1 (quatro pixels)
ponto = Point(300, 300)
ponto.setFill("Blue")
ponto.draw(janela)

# Desenhando pontos método-2 (um pixel)
janela.plot(320,320,"Red")

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
'''