from turtle import Turtle, Screen
screen = Screen()
class Snake:
    def __init__(self):
        self.snake = []
        self.starting_pos =  [(0,0), (-20,0), (-40,0)]
        self.starting_body()      
        self.key_list = {
        "w": self.up,
        "a": self.left,
        "s": self.down,
        "d": self.right    }
        self.direction()
    # Functions that set the snake Direction
    def up(self):
        self.snake[0].setheading(90)
        print("Snake goes up")  
    def down(self):
        self.snake[0].setheading(270)
        print("Snake goes down")  
    def left (self):
        self.snake[0].setheading(180)
        print("Snake goes left")  
    def right(self):
        self.snake[0].setheading(0)
        print("Snake goes right ")  
    def starting_body(self):
        """Creating the initial Snake Body from 3 squares appended in the "snake" list"""
        for pos in self.starting_pos:
            self.add_segment(pos)
    def direction(self):
        """Defines the direction of the snake motion"""
        for key, func in self.key_list.items():
            screen.onkey(func, key)  
        screen.listen()  # Listen for the keypress events
    def move(self):
        """Moves the snake forward by updating each segment's position.
        Each segment follows the segment in front of it, starting from the tail 
        to the second segment, while the head moves forward by 20 units.
        """
        for segment in range(len(self.snake)-1,0,-1):
            new_x = self.snake[segment-1].xcor()
            new_y = self.snake[segment-1].ycor()
            self.snake[segment].goto(new_x,new_y)
        self.snake[0].fd(20)
        
    def add_segment(self, pos):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

