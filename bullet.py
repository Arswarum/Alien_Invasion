import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Clas for controlling bullets fired by a ship.
    """
    def __init__(self, ai_settings, screen, ship):
        """
        Creates a bullet object at the current ship position.
        """
        super(Bullet, self).__init__()
        self.screen = screen
        # Creating a bullet in position (0,0) and assigning the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Bullet position stored in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        Moves the bullet up the screen.
        """
        # Update bullet position in float format
        self.y -= self.speed_factor
        # Rect position update
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw bullets on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)