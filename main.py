from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    
    if snake.snake[0].distance(food) < 15:
        print("Yum")
        food.rd_coor()

    time.sleep(0.075)

screen.exitonclick()
