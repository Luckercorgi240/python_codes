import turtle
t = turtle.Pen()
def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
    
print('How big do you want the square to be?')
size = input()
print('Type True or False')
filled = input()
mysquare(size, filled)