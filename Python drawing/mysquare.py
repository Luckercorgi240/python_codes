import turtle
t = turtle.Pen()
def mysquare(size, filled, color):
    t.fillcolor(color)
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
    turtle.done()
print('How big do you want the square to be?')
size = input()
size = int(size)
print('Type True or False')
filled = input()
filled = bool(filled)    
print('What color do you want your square to be?')
color = input()
color = str(color)
if filled == False:
    print('IF YOU TYPE FALSE THE PROGRAM WILL NOT DRAW THE SQUARE YOU WANTED. PLEASE TYPE TRUE.')
mysquare(size, filled, color)