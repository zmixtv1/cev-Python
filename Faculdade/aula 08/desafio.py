from graphics import *
import time

janela = GraphWin("linha pontilhada", 600, 600)

# Diagonal principal
for posicao in range(0, 599 ,  7):
  ponto = Point(posicao, 300)
  ponto.setFill("Red")
  ponto.draw(janela)
  time.sleep(0.01)

janela.getMouse()
janela.close()
