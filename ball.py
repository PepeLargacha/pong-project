from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = -10
        self.spleep = 0.09

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        self.spleep *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.sleep = 0.09

