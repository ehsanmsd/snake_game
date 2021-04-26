from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=SCORE_ALIGNMENT, font=SCORE_FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
