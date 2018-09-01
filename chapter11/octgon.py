import turtle
t = turtle.Pen()
def octgon(color):
    t.color(color)
    t.begin_fill()
    for x in range(10):
        t.forward(75)
        t.left(360/8)
    t.end_fill()
    t.color('black')
    t.pensize(2)
    for x in range(10):
        t.forward(75)
        t.left(360/8)
    turtle.done()
        
color = input('Please type in a color ')
octgon(color)