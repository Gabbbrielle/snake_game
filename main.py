from turtle import *
from scoreboard import Score
from snake import Snake
from food import Food

mode('standard')
import time

screen = Screen()
screensize(canvwidth=600, canvheight=600, bg='black')
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
        score.timer()
    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        game_on = False
        score.game_over()






screen.exitonclick()
