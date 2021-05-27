from graphics import *
win = GraphWin("Um oval", 600, 600)
o = Oval(Point(100,120), Point(200,180))
o.setOutline("red")
o.setFill("orange")
o.draw(win)

r = Rectangle(Point(100, 120), Point(200, 180))
r.draw(win)

p = Polygon(Point(400,100), Point(450,120), Point(460,160), Point(490,210))
p.setOutline("blue")
p.setFill("violet")
p.draw(win)

t = Text(Point(300, 300), "Lógica de Programação")
t.setOutline("blue")
t.setSize(18)
t.draw(win)

t = Text(Point(50, 400), "Nome:")
t.setOutline("blue")
t.setSize(18)
t.draw(win)

inp = Entry(Point(250, 400), 30)
inp.setFill("White")
inp.draw(win)

win.getMouse()

print(inp.getText())

win.getMouse()
win.close()

