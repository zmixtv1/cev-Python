import time
from graphics import *
win = GraphWin("Contagem", 600, 600)

for num in range(0, 600, 2):

    t = Text(Point(num, 400), "hoje é pra entregar só esses 2 exercicios ou tem que entregar do outro slide tambem? no primeiro exercicios os quadrados tem que ter 50 pixeis de lado, no caso sao 50 pontos de lado? ou é diferente?ah sim ok")
    t.setOutline("blue")
    t.setSize(10)
    t.draw(win)
    time.sleep(0.1)
    t.undraw()

win.getMouse()
win.close()