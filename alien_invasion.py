import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_funktions as gf

def run_game():

    # initiates a pygame, settings and creates a screen object

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen) # ship creation
    alien = Alien(ai_settings, screen) # alien creation
    # Creating a group to store bullets
    bullets = Group()

    # launch of the main game loop

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # mouse and keyboard event tracking
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
run_game()