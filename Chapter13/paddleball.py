from tkinter import *
import random
import time

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
speed = input('How fast do you want the ball to be? (between 1 and 5)')
while RepresentsInt(speed) != True or int(speed) < 0 or int(speed) > 5:
    print('Your number is either not a number or is out of range. Please try again with a different number')
    speed = input('How fast do you want the ball to be? (between 1 and 5)')

speed = int(speed)

# speed = input('How fast do you want the ball to be? (between 1 and 5) ')
# while RepresentsInt(speed) != True:
#     print('Please enter a number')
#     speed = input('How fast do you want the ball to be? (between 1 and 5) ')
        
# while int(speed) < 0 or int(speed) > 5:
#     print('Your speed is too fast or too slow please change')
#     speed = input('How fast do you want the ball to be? (between 1 and 5) ')
#     while RepresentsInt(speed) != True:
#         print('Please enter a number')
#         speed = input('How fast do you want the ball to be? (between 1 and 5) ')

# speed = int(speed)
            
class Ball:
    def __init__(self, canvas, paddle, color, speed):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = starts[4]
        # self.y = speed
        # self.x = speed
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.speed = speed
        self.score = 0
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.speed
            # self.speed = self.speed + 1
        if pos[3] >= self.canvas_height:
            self.y = -self.speed
            # self.speed = self.speed + 1
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -self.speed
            self.score = self.score + 10
            # self.speed = self.speed + 1
        if pos[0] <= 0:
            self.x = self.speed
            # self.speed = self.speed + 1
        if pos[2] >= self.canvas_width:
            self.x = -self.speed
            # self.speed = self.speed + 1

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -5
    def turn_right(self, evt):
        self.x = 5

tk = Tk()
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
tk.title('Game')
canvas.pack()
tk.update()
color = input('What color do you want the ball to be? ')
# color2 = input('What color do you want the ball to be? ')
# color3 = input('What color do you want the ball to be?')
paddle = Paddle(canvas, 'blue')
ball1 = Ball(canvas, paddle, color, speed)
# ball2 = Ball(canvas, paddle, color2, speed)
# ball3 = Ball(canvas, paddle, color3, speed)
time.sleep(3)
previous_text_id = 0
while 1:
    if ball1.hit_bottom == False: #and ball2.hit_bottom == False and ball3.hit_bottom == False:
        ball1.draw()
        # ball2.draw()
        # ball3.draw()
        paddle.draw()
        score = str(ball1.score)
        if previous_text_id != 0:
            canvas.delete(previous_text_id)
        text_id = canvas.create_text(390, 10, text=score, font=('Systemfixed', 15))
        previous_text_id = text_id
    else:
        canvas.create_text(200, 200, text='GAME OVER!!', fill='red', font=('Helvetica', 30))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)