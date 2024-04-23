import random
from turtle import Turtle

STARTING_POINT = (-400, 279)


class SecretAlien(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('./img/super_ship.gif')
        self.penup()
        self.hideturtle()
        self.move_speed = 5
        self.goto(STARTING_POINT)

    def move(self):
        self.forward(self.move_speed)
        if self.xcor() > 370:
            self.hideturtle()
            self.goto(STARTING_POINT)

    def trigger(self):
        random_chance = random.randint(1, 40)
        if random_chance == 1 and not self.isvisible():
            self.goto(STARTING_POINT)
            self.showturtle()

    def restart(self):
        self.hideturtle()
        self.goto(STARTING_POINT)
