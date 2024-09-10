from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)

def up(snk):
    snk.setheading(90)
    print("Snake goes up")  
def down(snk):
    snk.setheading(270)
    print("Snake goes down")  
def left (snk):
    snk.setheading(180)
    print("Snake goes left")  
def right(snk):
    snk.setheading(0)
    print("Snake goes right ")  

snake = []
starting_pos = [(0,0), (-20,0), (-40,0)]
def starting_body():
    for pos in starting_pos:
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        snake.append(segment)

starting_body()
screen.listen()
key_list = {
    "w": up,
    "a": left,
    "s": down,
    "d": right
} 
game_is_on = True
for key, func in key_list.items():
    screen.onkey(lambda f=func: f(snake[0]), key)

while game_is_on:
    screen.update()
    for segment in range(len(snake)-1,0,-1):
        new_x = snake[segment-1].xcor()
        new_y = snake[segment-1].ycor()
        snake[segment].goto(new_x,new_y)
        time.sleep(.1)

    snake[0].fd(20)

screen.exitonclick()
