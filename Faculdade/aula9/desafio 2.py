from graphics import *
from graphics import *
from time import sleep
import random
janela = GraphWin("Quadrados ...", 600, 600)
janela.setBackground("gray")
tam = 3
for c in range(66):
    circulo = Circle(Point(300, 300), tam)
    cor = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    circulo.setFill(cor)
    circulo.setOutline("black")
    circulo.draw(janela)
    sleep(0.1)
    tam += 3
    if tam == 198:
        break

janela.getMouse()
janela.close()
