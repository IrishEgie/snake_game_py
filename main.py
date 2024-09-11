from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)

s_width = screen.window_width()/2
s_height = screen.window_height()/2

snake = Snake()
snake_head = snake.snake[0]

food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    
    if snake_head.distance(food) < 15:
        print("Yum")
        food.rd_coor()
        snake.extend()
        score.write_score()
    if (abs(snake_head.xcor()) > s_width or abs(snake_head.ycor()) > s_height):
            score.write_game_over()
            game_is_on = False
    for segment in snake.snake[2:]:
        if snake_head.distance(segment)<10:
            score.write_game_over()
            game_is_on = False

    time.sleep(0.1)

screen.exitonclick()
