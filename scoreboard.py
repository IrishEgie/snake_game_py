from turtle import Turtle
FONT = ('Courier', 15, 'bold')

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
        self.write(f"Score: {self.SCORE} ", move=False, align='center', font=FONT)
        return self.SCORE
    def write_game_over(self):
        self.game_over = Turtle()
        self.game_over.penup()
        self.game_over.hideturtle()
        self.game_over.color("white")
        self.game_over.write("GAME OVER",move=False, align='center', font=FONT)
        print("Game over")