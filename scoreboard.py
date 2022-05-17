from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 36, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def write_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(-40, 275)
        self.pendown()
        self.fd(40)
        self.penup()
        self.goto(60, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
