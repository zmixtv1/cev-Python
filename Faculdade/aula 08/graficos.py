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

from graphics import *
import time

janela = GraphWin("Fazer um X na tela ...", 600, 600)

# Diagonal principal
for posicao in range(600 ):
   ponto = Point(posicao, posicao)
   ponto.setFill(color_rgb(150, 230, 150))
   ponto.draw(janela)
   time.sleep(0.01)

   ponto = Point(599-posicao, posicao)
   ponto.setFill(color_rgb(150, 230, 150))
   ponto.draw(janela)

   ponto = Point(posicao, 599)
   ponto.setFill(color_rgb(150, 255, 150))
   ponto.draw(janela)
'''
   ponto = Point(399 - posicao, 0 )
   ponto.setFill(color_rgb(150, 255, 150))
   ponto.draw(janela)

   ponto = Point(0 ,399 - posicao)
   ponto.setFill(color_rgb(150, 255, 150))
   ponto.draw(janela)

   ponto = Point(398, posicao)
   ponto.setFill(color_rgb(150, 255, 150))
   ponto.draw(janela)


# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()

'''