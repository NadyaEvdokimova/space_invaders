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
        self.clear()
        self.goto(-190, -290)
        self.write(f'Score: {self.score}', align="right",
                   font=("Courier", 20, "normal"))

    def point(self, score):
        self.score += score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -130)
        self.write(f"GAME OVER\nYour Score is {self.score}", align="center",
                   font=("Courier", 20, "normal"))

    def win(self):
        self.goto(0, 0)
        self.write(f"You won!\nYour Score is {self.score}", align="center",
                   font=("Courier", 20, "bold"))
