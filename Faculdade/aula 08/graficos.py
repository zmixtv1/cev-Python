
from graphics import *
import random
import time
numero_janelas = random.randrange(10, 300)
for i in range(numero_janelas):
   largura = random.randrange(100, 600)
   altura = random.randrange(100, 400)
   vermelho = random.randrange(0, 256)
   verde = random.randrange(0, 256)
   azul = random.randrange(0, 256)

   jan = GraphWin("Janela-" + str(i), largura, altura)
   jan.setBackground(color_rgb(vermelho, verde, azul))

jan.getMouse()
