from graphics import *
import time

janela = GraphWin("Fazer um X na tela ...", 600, 600)

# Diagonal principal
for posicao in range(0, 600 ,  5):
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

