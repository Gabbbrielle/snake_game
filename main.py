from turtle import *
from scoreboard import Score
from snake import Snake
from food import Food

mode('standard')
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('Snake-it!')
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_refresh()
        snake.get_bigger()
        # score.timer()
    if snake.head.xcor() < -375 or snake.head.xcor() > 370 or snake.head.ycor() < -310 or snake.head.ycor() > 320:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()






screen.exitonclick()
