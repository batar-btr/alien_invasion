import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """The main class to manage game behavior and assets."""

    def __init__(self):
        """Init game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # surface

        # =========================FullScreen============================
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # ===============================================================

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Run main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()
            self.clock.tick(60)

    def _fire_bullet(self):
        """Create a new bullet and add to group bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_events(self):
        """Listen keybord and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Update image and new screen"""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        # Show last drawed screen
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Reacts to keydown"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reacts to keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    # Create game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
