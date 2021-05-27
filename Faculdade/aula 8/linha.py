from graphics import *

janela = GraphWin("Linhas ...", 600, 400)

# Desenhando linhas
linha = Line(Point(10, 100), Point(590, 100))
linha.setFill("green")
linha.setArrow("both")
linha.draw(janela)

outraLinha = Line(Point(10, 200), Point(590, 390))
outraLinha.setFill("red")
outraLinha.setArrow("last")
outraLinha.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
