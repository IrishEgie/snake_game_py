from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)
starting_pos = [(0,0), (-20,0), (-40,0)]

snake = []

def starting_body():
    for pos in starting_pos:
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        snake.append(segment)

starting_body()

game_is_on = True

while game_is_on:
    screen.update()
    for segment in range(3,0,-1):
        
        time.sleep(.1)
        x_edge = ((screen.window_width())/2)+20
        y_edge = (screen.window_width())/2
        if segment.xcor() >= x_edge:
            segment.goto(x_edge*-1, y_edge*0)

screen.exitonclick()
