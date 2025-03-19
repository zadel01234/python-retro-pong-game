from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.faster = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.faster *= 0.7

    def bounce_x(self):
        self.x_move *= -1
        self.faster *= 0.9

    def ball_refresh(self):
        self.home()
        self.x_move *= -1
        self.y_move *= -1
        self.faster = 0.1


