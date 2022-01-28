from turtle import Turtle
initial_position = [(0, 0), (-20., 0), (-20, 0)]

move_forwards = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.list_turtle = []
        self.crate_snake()
        self.head = self.list_turtle[0]

    def crate_snake(self):
        for position in initial_position:
            self.add_size(position)

    def add_size(self,position):
        timmy = Turtle()
        timmy.penup()
        timmy.color("white")
        timmy.shape("square")
        timmy.goto(position)
        self.list_turtle.append(timmy)
    def extend(self):
        self.add_size(self.list_turtle[-1].position())

    def move(self):
        for index in range(len(self.list_turtle) - 1, 0, -1):
            x_axis = self.list_turtle[index - 1].xcor()
            y_axis = self.list_turtle[index - 1].ycor()
            self.list_turtle[index].goto(x_axis, y_axis)
        self.head.forward(move_forwards)

    def up(self):
        if self.head.heading() != DOWN:
            self.list_turtle[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def right_reset(self):
        y_cor = self.head.ycor()
        if self.head.xcor() > 300:
            self.head.goto(-300, y_cor)
    def left_reset(self):
        y_cor = self.head.ycor()
        if self.head.xcor() < -300:
            self.head.goto(300, y_cor)
    def y_rest(self):
        x_cor = self.head.xcor()
        if self.head.ycor() > 250:
            self.head.goto(x_cor, -250)
        if self.head.ycor() < -250:
            self.head.goto(x_cor, 250)