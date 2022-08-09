from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(410, 250)
        self.clear()
        self.write(f"Score: {self.score} ", align="right", font=("Courier", 30, "normal"))

    def score_up(self):
        self.score += 1


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.lives = 5
        self.update_lives()

    def update_lives(self):
        self.goto(-390, 250)
        self.clear()
        self.write(f"Lives: {self.lives} ", align="left", font=("Courier", 30, "normal"))

    def live_down(self):
        self.lives -= 1


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.text = 'Game Over!'

    def show_text(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"{self.text}", align="center", font=("Courier", 30, "normal"))
