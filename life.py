from turtle import Turtle


class Life:
    def __init__(self):
        self.lives = []
        self.get_lives()

    def get_lives(self):
        for x_pos in range(230, 300, 30):
            life = Turtle()
            life.shape('./img/life.gif')
            life.penup()
            life.goto((x_pos, -275))
            self.lives.append(life)

    def remove_life(self):
        lives_number = len(self.lives)
        self.lives[lives_number - 1].ht()
        del self.lives[lives_number - 1]
