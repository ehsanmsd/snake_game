from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=SCORE_ALIGNMENT, font=SCORE_FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
