import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Bullets control class"""

    def __init__(self, ai_game: "AlienInvasion"):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Creating a bullet at (0,0) position and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The bullet position is stored in float format
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet upwards"""
        self.y -= self.settings.bullet_speed

        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
