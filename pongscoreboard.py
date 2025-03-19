from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.homescore = 0
        self.awayscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(200, 260)
        self.write(f'score {self.awayscore}', align = "center", font = ('Arial', 24, "normal"))
        self.goto(-200, 260)
        self.write(f'score {self.homescore}', align = "center", font = ("Arial", 24, "normal"))


    def awaywin(self):
        self.awayscore += 1
        self.update_scoreboard()

    def homewin(self):
        self.homescore += 1
        self.update_scoreboard()

    def winner(self):
        if self.homescore == 5:
            self.goto(0,0)
            self.write(f"Home is the winner!!", align = "center",font = ("Arial", 24, "normal") )
            return False

        elif self.awayscore == 5:
            self.goto(0,0)
            self.write("away is the winner!!", align = "center", font = ("Arial",24, "normal"))
            return False
        
        else:
            return True
