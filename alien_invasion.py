import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # initialise game and create screen object
    pygame.init()

    ai_settings = Settings()

    # set screen size
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
         
    # set window title
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make the player ship
    ship = Ship(ai_settings,screen)
    # Make groups to store bullets and aliens in
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    clock = pygame.time.Clock()
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings,screen, stats, sb, play_button, ship, 
                aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, 
                    ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                    bullets, play_button)

        clock.tick(300)

if __name__ == "__main__":
    run_game()
