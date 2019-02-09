import turtle
t = turtle.Pen()
t.color('blue')
t.forward(100)   
def d():
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)

for x in range(36):
     d()
     t.left(10)
turtle.done()
