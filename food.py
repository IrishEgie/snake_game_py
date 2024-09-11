from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(.5,.5,0)
        self.color("yellow")
        self.rd_coor()

    def rd_coor(self):
        self.random_x = rd.randint(-280,280)
        self.random_y = rd.randint(-280,280)
        self.goto(self.random_x, self.random_y)
