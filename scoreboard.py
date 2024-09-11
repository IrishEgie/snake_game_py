from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.SCORE = -1
        self.write_score()

    def write_score(self):
        self.clear()
        self.SCORE +=1
        self.write(f"Score: {self.SCORE} ", move=False, align='center', font=('Consolas', 10, 'bold'))
        
        return self.SCORE
    