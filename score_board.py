from turtle import Turtle
alignment = "center"
font = ("Arial", 15, "normal")


class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        with open("high score.txt") as file:
            self.high_score = file.read()
        self.score = 0
        # self.high_score = self.context
        self.color("white")
        self.penup()
        self.goto(0,230)
        self.write(f"Score = {self.score} High Score:{self.high_score} ", align=alignment, font=font)
        self.hideturtle()

    def current_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score = {self.score} High Score:{self.high_score} ", align=alignment, font=font)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))

    def highscore(self):
        if int(self.high_score) <= self.score:
            self.clear()
            self.high_score = self.score
            self.write(f"Score = {self.score} High Score:{self.high_score} ", align=alignment, font=font)
            with open("high score.txt", mode="w") as file:
                file.write(f"{self.score}")
