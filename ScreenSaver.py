from tkinter import *
from random import randint


class Balls:

    def __init__(self, canvas):
        self.canvas = canvas
        self.screenwidth = canvas.winfo_screenwidth()
        self.screenheight = canvas.winfo_screenheight()
        self.radius = randint(50, 100)
        self.x_coord = randint(self.radius, self.screenwidth - self.radius)
        self.y_coord = randint(self.radius, self.screenheight - self.radius)
        self.x_speed = randint(5, 15)
        self.y_speed = randint(5, 15)
        self.color = self.randcolors()
        self.x1 = self.x_coord - self.radius
        self.y1 = self.y_coord - self.radius
        self.x2 = self.x_coord + self.radius
        self.y2 = self.y_coord + self.radius
        self.ball = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.color)

    @staticmethod
    def randcolors():
        global color
        randval = randint(0, 9)
        if randval == 0:
            color = "red"
        elif randval == 1:
            color = "orange"
        elif randval == 2:
            color = "yellow"
        elif randval == 3:
            color = "green"
        elif randval == 4:
            color = "blue"
        elif randval == 5:
            color = "purple"
        elif randval == 6:
            color = "black"
        elif randval == 7:
            color = "cyan"
        elif randval == 8:
            color = "grey"

        return color

    def moveball(self):
        self.findboundry()
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed
        self.canvas.move(self.ball, self.x_speed, self.y_speed)

    def findboundry(self):
        if not self.radius < self.x_coord < self.screenwidth - self.radius:
            self.x_speed = -self.x_speed

        if not self.radius < self.y_coord < self.screenheight - self.radius:
            self.y_speed = -self.y_speed


class Screen:

    balls = []

    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.6)
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=1, fill=BOTH)
        self.ball = Balls(self.canvas)
        for ball in range(15):
            self.balls.append(Balls(self.canvas))
        self.moveballs()
        self.root.bind('<Escape>', quit)
        self.root.mainloop()

    def moveballs(self):
        for ball in self.balls:
            ball.moveball()
        self.root.after(30, self.moveballs)


Screen()
