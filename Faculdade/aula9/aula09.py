
from graphics import *

janela = GraphWin("Retângulos ...", 600, 400)

# Desenhando Retângulos
retangulo = Rectangle(Point(10, 10), Point(590, 100))
retangulo.setFill("brown")
retangulo.setOutline("black")
retangulo.draw(janela)

outroRetangulo = Rectangle(Point(500, 110), Point(590, 390))
outroRetangulo.setFill("orange")
outroRetangulo.setOutline("red")
outroRetangulo.draw(janela)

terceiroRetangulo = Rectangle(Point(10, 110), Point(490, 390))
terceiroRetangulo.setFill("green")
terceiroRetangulo.setOutline("blue")
terceiroRetangulo.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()


#Circulo

from graphics import *

janela = GraphWin("Círculos ...", 600, 400)
janela.setBackground("gray")

retangulo = Rectangle(Point(200,230), Point(50, 180))
retangulo.setFill("black")
retangulo.setOutline("white")
retangulo.draw(janela)

cabo = Circle(Point(80,204), 15)
cabo.setFill("gray")
cabo.setOutline("black")
cabo.draw(janela)

azul = Circle(Point(299, 199), 110)
azul.setFill("blue")
azul.setOutline("black")
azul.draw(janela)

# Desenhando Círculos
circulo = Circle(Point(299,199), 90)
circulo.setFill("white")
circulo.setOutline("brown")
circulo.draw(janela)

menor = Circle(Point(299, 199), 60)
menor.setFill("orange")
menor.setOutline("red")
menor.draw(janela)


# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()


from graphics import *
import time, random

janela = GraphWin("Círculos aleatórios ...", 600, 400)

for i in range(500):
   centro = Point(random.randrange(0, 600), random.randrange(0, 400))
   raio = random.randrange(10, 50)
   circulo = Circle(centro, raio)
   circulo.setOutline("blue")
   cor = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
   circulo.setFill(cor)
   circulo.draw(janela)
   time.sleep(0.1)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
