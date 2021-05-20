from graphics import *
from time import sleep
import random
janela = GraphWin("Quadrados ...", 600, 600)
janela.setBackground("gray")
tam = 3
for c in range(67):
    circulo = Circle(Point(300, 300), tam)
    cor = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    circulo.setFill(cor)
    circulo.setOutline("black")
    circulo.draw(janela)
    tam += 3
    print(c)
    sleep(0.1)
    if tam == 199:
        break

janela.getMouse()
janela.close()
