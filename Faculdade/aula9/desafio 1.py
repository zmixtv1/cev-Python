from graphics import *
janela = GraphWin("Quadrados ...", 600, 600)
janela.setBackground("gray")

retangulo = Rectangle(Point(30, 200), Point(200,350))
retangulo.setFill("green")
retangulo.setOutline("black")
retangulo.draw(janela)

segundo_retangulo = Rectangle(Point(360, 200), Point(210,350))
segundo_retangulo.setFill("yellow")
segundo_retangulo.setOutline("black")
segundo_retangulo.draw(janela)

terceiro_retangulo = Rectangle(Point(530, 200), Point(370,350))
terceiro_retangulo.setFill("red")
terceiro_retangulo.setOutline("black")
terceiro_retangulo.draw(janela)

janela.getMouse()
janela.close()