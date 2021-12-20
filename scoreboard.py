from turtle import Turtle
class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("arial", 24, "normal"))
        self.hideturtle()

    def Game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game over", align="center", font=("arial", 24, "normal"))




    def renew(self,i):
        self.clear()
        self.write(f"Score: {self.score + i}", align="center", font=("arial", 24, "normal"))


