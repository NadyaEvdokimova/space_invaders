import time
from turtle import Screen
from gun import Gun
from alien import Alien
from bunker import Bunker
from fire import Fire
from scoreboard import Scoreboard
from life import Life
from secret_alien import SecretAlien

screen = Screen()
screen.title("Space Invaders")
screen.setup(width=700, height=600)
screen.bgpic("img/bg_dark.gif")
screen.register_shape('./img/ship.gif')
screen.register_shape('./img/player_ship.gif')
screen.register_shape('./img/life.gif')
screen.register_shape('./img/super_ship.gif')
screen.tracer(0)
gun = Gun()
aliens = Alien()
bunker = Bunker()
scoreboard = Scoreboard()
life = Life()
secret_alien = SecretAlien()
fires = []
alien_fires = [] 
alien_fire_delay = 2000


# Create fire of player and of aliens
def create_fire(x, y):
    new_fire = Fire(x, y, 90, "red")
    new_fire.start_movement()
    fires.append(new_fire)


def alien_fire():
    alien_fire_object = aliens.fire()
    alien_fires.append(alien_fire_object)
    screen.update()
    screen.ontimer(alien_fire, alien_fire_delay)


# Make gun movement
screen.listen()
screen.onkeypress(gun.right_move, "Right")
screen.onkeyrelease(gun.right_move_end, "Right")
screen.onkeypress(gun.left_move, "Left")
screen.onkeyrelease(gun.left_move_end, "Left")
screen.onkey(lambda: create_fire(gun.xcor(), gun.ycor()), "space")


# Game starts
game_is_on = True
alien_fire()
while game_is_on:
    screen.update()
    aliens.move_aliens()
    secret_alien.move()
    secret_alien.trigger()
    time.sleep(0.1)

    # Fire handling of gun
    for fire in list(fires):
        if fire.isvisible():
            fire.move()
            # Check if fire reaches the top
            if fire.ycor() > screen.window_height() / 2:
                fire.ht()
                fires.remove(fire)
        # Check collision of gun's fire with alien
        for alien in aliens.aliens:
            if fire.distance(alien) < 20:
                alien_index = aliens.aliens.index(alien)
                aliens.exclude_alien(alien_index)
                scoreboard.point(10)
                if fire in fires:
                    fire.ht()
                    fires.remove(fire)
            if len(aliens.aliens) == 0:
                screen.update()
                scoreboard.win()
                game_is_on = False
        if fire.distance(secret_alien) < 20:
            secret_alien.restart()
            scoreboard.point(20)
        # Check collision of gun's fire with the bunker
        for bunker_part in list(bunker.whole_bunker):
            if fire.distance(bunker_part) < 15:
                part_index = bunker.whole_bunker.index(bunker_part)
                bunker.remove_bunker(bunker_part, part_index)
                if fire in fires:
                    fire.ht()
                    fires.remove(fire)
    # Fire handling of alien
    for alien_fire_obj in list(alien_fires):
        if alien_fire_obj.isvisible():
            alien_fire_obj.move()
            # Check if alien fire reaches the bottom
            if alien_fire_obj.ycor() < -screen.window_height() / 2:
                alien_fire_obj.ht()
                alien_fires.remove(alien_fire_obj)
        # Check collision of alien's fire with the gun
        if alien_fire_obj.distance(gun) < 20:
            life.remove_life()
            alien_fire_obj.ht()
            alien_fires.remove(alien_fire_obj)
            # Check how many lives left
            if len(life.lives) == 0:
                game_is_on = False
                screen.update()
                scoreboard.game_over()

        # Check collision of alien's fire with the bunker
        for bunker_part in list(bunker.whole_bunker):
            if alien_fire_obj.distance(bunker_part) < 15:
                part_index = bunker.whole_bunker.index(bunker_part)
                bunker.remove_bunker(bunker_part, part_index)
                if alien_fire_obj in alien_fires:
                    alien_fire_obj.ht()
                    alien_fires.remove(alien_fire_obj)
    # Check if the aliens are close to the bunker
    for alien in aliens.aliens:
        for bunker_part in list(bunker.whole_bunker):
            if alien.distance(bunker_part) < 20:
                part_index = bunker.whole_bunker.index(bunker_part)
                bunker.remove_bunker(bunker_part, part_index)
        if alien.ycor() == -220:
            game_is_on = False
            screen.update()
            scoreboard.game_over()


screen.exitonclick()
