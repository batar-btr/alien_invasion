import pygame


class Ship:
    """Ship control class"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/custom_ship2.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.y = self.screen.get_height() - 125
        self.x = float(self.rect.x)

        # Ship moving flags - start from not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position according to ship moving flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw ship in the current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put the ship into tht bottom screen center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
