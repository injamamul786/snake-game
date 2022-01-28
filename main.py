from turtle import Screen
from food import Food
from score_board import Score_board
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
score_board = Score_board()
snake = Snake()
food = Food()
food.refresh()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.current_score()
        snake.extend()
    # detect position with wall
    snake.right_reset()
    snake.left_reset()
    snake.y_rest()
    score_board.highscore()
    for segment in snake.list_turtle[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.gameover()


screen.exitonclick()
