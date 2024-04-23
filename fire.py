from turtle import Turtle


class Fire(Turtle):
    def __init__(self, x_cor, y_cor, angle, color):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.y_move = 20
        self.angle = angle
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=0.2, stretch_len=1)
        self.penup()
        self.hideturtle()

    def start_movement(self):
        self.goto(self.x_cor, self.y_cor)
        self.showturtle()

    def move(self):
        self.setheading(self.angle)
        self.forward(self.y_move)

    def reset_fire(self):
        self.hideturtle()

    def del_fire(self):
        self.ht()
        del self
