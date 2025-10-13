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
            """Listen keybord and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Show last drawed screen
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Create game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
