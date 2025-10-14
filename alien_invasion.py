import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """The main class to manage game behavior and assets."""

    def __init__(self):
        """Init game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # surface

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Run main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Listen keybord and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update image and new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Show last drawed screen
        pygame.display.flip()


if __name__ == "__main__":
    # Create game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
