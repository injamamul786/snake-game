from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.3, stretch_len=0.3)
        self.color("red")

    def refresh(self):
        x_axis = randint(-280, 280)
        y_axis = randint(-240, 240)
        self.goto(x_axis, y_axis)