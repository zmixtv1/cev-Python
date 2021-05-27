from graphics import *
from time import sleep
janela = GraphWin("Desafio", 800, 800)

outraLinha = Line(Point(0, 200), Point(830, 200))
outraLinha.setFill("red")
outraLinha.setArrow("last")
outraLinha.draw(janela)

outraLinha = Line(Point(0, 400), Point(830, 400))
outraLinha.setFill("red")
outraLinha.setArrow("last")
outraLinha.draw(janela)

t = Text(Point(150, 300), "Digite algo:")
t.setOutline("blue")
t.setSize(18)
t.draw(janela)
inp = Entry(Point(350, 300), 30)
inp.draw(janela)

tecla=''
while tecla != 'Escape':
   tecla = janela.getKey()

   frase = inp.getText()

   if tecla == 'Return':
       t = Text(Point(400, 340), f"Você digitou: {inp.getText()}")
       t.setOutline("red")
       t.setSize(18)
       t.draw(janela)
       sleep(2)
       t.undraw()

if tecla == "Escape":
    janela.close()
