import sys

import pygame


class AlienInvasion:
    """The main class to manage game behavior and assets."""

    def __init__(self):
        """Init game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # surface
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run main game loop"""
        while True:
            """Listen keybord and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show last drawed screen
            pygame.display.flip()


if __name__ == "__main__":
    # Create game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
