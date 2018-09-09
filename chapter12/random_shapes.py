from tkinter import Canvas, Tk
import random
import time
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
# colorlist = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
def random_shapes():
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = random.randint(0, 400)
    y2 = random.randint(0, 400)
    x3 = random.randint(0, 400)
    y3 = random.randint(0, 400)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    colorval = "#%02x%02x%02x" % color
    # a = len(colorlist)-1
    # canvas.create_rectangle(x1, y1, x2, y2, fill = colorlist[random.randint(0, a )])
    # canvas.create_rectangle(x1, y1, x2, y2, fill = colorval)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = colorval)

num = input('How many shapes do you want? ')
num = int(num)
appear = input('How fast do you want each shape to appear?')
appear = float(appear)
for x in range(1, num):
    random_shapes()
    tk.update()
    time.sleep(appear)
tk.mainloop()