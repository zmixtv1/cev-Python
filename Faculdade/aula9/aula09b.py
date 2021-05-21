from graphics import *
import time , random
whin = GraphWin("contagem", 480,480)

for num in range(0, 100):
    cor = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    t = Text(Point(230, 200), str(num))
    t.setOutline(cor)
    t.setSize(30)
    t.draw(whin)
    time.sleep(.1)
    t.undraw()

whin.getMouse()
whin.close()
