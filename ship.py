import pygame

class Ship():
    def __init__(self, screen):
        """
        initializes the ship and sets its starting position
        :param screen: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        self.screen = screen

        # вownload image of the ship and receiving a rectangle

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # each new ship appears at the bottom of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        # draws a ship in the current position
        self.screen.blit(self.image, self.rect)