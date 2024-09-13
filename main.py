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

last_move_time = time.time()  # Track the time of the last snake movement

MOVE_INTERVAL = 0.08  # Controls how often the snake moves (in seconds)
FRAME_RATE = 0.01  # Controls how often the screen updates

game_is_on = True
while game_is_on:
    
    current_time = time.time()

    # Check if enough time has passed to move the snake
    if current_time - last_move_time >= MOVE_INTERVAL:
        snake.move()
        last_move_time = current_time
    
    if snake_head.distance(food) < 15:
        print("Yum")
        food.rd_coor()
        snake.extend()
        score.write_score()
    if (abs(snake_head.xcor()) > s_width or abs(snake_head.ycor()) > s_height):
            score.reset_score()
            snake.reset_snake()
            snake_head = snake.snake[0]
            
    for segment in snake.snake[2:]:
        if snake_head.distance(segment)<10:
            score.reset_score()
            snake.reset_snake()
            snake_head = snake.snake[0]
            
    screen.update()
    time.sleep(FRAME_RATE)

screen.exitonclick()
