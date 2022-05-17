from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.penup()
        self.goto(cord)

    def set_player(self, player=1):
        if player == 1:
            self.goto(x=-380, y=self.pos()[1])
        else:
            self.goto(x=380, y=self.pos()[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)