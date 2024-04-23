import random
from turtle import Turtle
from fire import Fire


class Alien:
    def __init__(self):
        self.aliens = []
        self.create_aliens()
        self.alien_fire_delay = 3000
        self.alien_speed = 5
        self.alien_direction = 1

    def create_aliens(self):
        for all_pos in range(50, 260, 50):
            for y_pos in range(all_pos, all_pos+20, 50):
                for position in range(-285, 70, 40):
                    alien = Turtle()
                    alien.shape('./img/ship.gif')
                    alien.seth(270)
                    alien.shapesize(stretch_wid=1, stretch_len=1)
                    alien.penup()
                    alien.color('yellow')
                    alien.goto(x=position, y=y_pos)
                    self.aliens.append(alien)

    def fire(self):
        random.shuffle(self.aliens)
        for alien in self.aliens:
            fire = Fire(alien.xcor(), alien.ycor(), 270, 'yellow')
            fire.start_movement()
            return fire

    def move_aliens(self):
        for alien in self.aliens:
            alien.setx(alien.xcor() + self.alien_speed * self.alien_direction)
        self.change_direction()

    def change_direction(self):
        for alien in self.aliens:
            if alien.xcor() >= 285 or alien.xcor() <= -285:
                self.alien_direction *= -1
                self.move_down()
                break

    def move_down(self):
        for alien in self.aliens:
            alien.sety(alien.ycor() - 20)

    def exclude_alien(self, del_alien):
        self.aliens[del_alien].ht()
        del self.aliens[del_alien]

