from turtle import Turtle


class Gun(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('./img/player_ship.gif')
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.seth(90)
        self.position = (20, -250)
        self.goto(self.position)
        self.move_left = False
        self.move_right = False

    def right_move(self):
        if self.xcor() < 285:
            self.move_right = True
            x_current = self.xcor()
            self.setx(x_current + 15)

    def right_move_end(self):
        if self.xcor() < 285:
            self.move_right = False

    def left_move(self):
        if self.xcor() > - 285:
            self.move_left = True
            x_current = self.xcor()
            self.setx(x_current - 15)

    def left_move_end(self):
        if self.xcor() > - 285:
            self.move_left = True
