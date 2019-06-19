import sys
import pygame
from settings import Settings
from ship import Ship
import game_funktions as gf

def run_game():

    # initiates a pygame, settings and creates a screen object

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen) # ship creation

    # launch of the main game loop

    while True:
        gf.check_events()  # mouse and keyboard event tracking
        gf.update_screen(ai_settings, screen, ship)
run_game()
