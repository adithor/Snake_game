from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial",12, "normal")

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.score}",align=ALIGNMENT,font= FONT)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"score: {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align= ALIGNMENT, font = FONT)


    def increase_score(self):
        self.score += 1
        self.write(f"score: {self.score}",align=ALIGNMENT,font= FONT)
        self.clear()       
        self.update_scoreboard()