from turtle import Turtle


class Bunker:
    def __init__(self):
        self.whole_bunker = []
        self.bunker()

    def bunker(self):
        for x_cor in range(-280, 250, 100):
            for y_pos in range(-180, -100, 30):
                for x_pos in range(x_cor, x_cor+60, 5):
                    bunker = Turtle('square')
                    bunker.shapesize(stretch_wid=1, stretch_len=1)
                    bunker.color('cornflowerblue')
                    bunker.penup()
                    bunker.goto(x=x_pos, y=y_pos)
                    self.whole_bunker.append(bunker)

    def remove_bunker(self, bunker_part, bunker_index):
        bunker_part.ht()
        del self.whole_bunker[bunker_index]

