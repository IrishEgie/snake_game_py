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

snake = Snake()
food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    
    if snake.snake[0].distance(food) < 15:
        print("Yum")
        food.rd_coor()
        score.write_score()
        


    time.sleep(0.1)

screen.exitonclick()
