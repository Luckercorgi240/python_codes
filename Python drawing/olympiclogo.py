import turtle
t = turtle.Pen()
for x in range(3):
    t.circle(50)
    t.up()
    t.forward(120)
    t.down()

t.up()
t.back(120)
t.back(60)
t.right(90)
t.forward(50)
t.left(90)
t.down()
t.circle(50)
t.up()
t.back(120)
t.down()
t.circle(50)
turtle.done()