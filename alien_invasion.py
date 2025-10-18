import sys
from time import sleep


import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        # =========================FullScreen============================
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # ===============================================================

        self.stats = GameStats(self)  # Instantiate Stats
        self.sb = ScoreBoard(self)  # Instantiate ScoreBoard
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color

        self._create_fleet()

        self.game_active = False

        # Creating Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Run main game loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _ship_hit(self):
        """Handle the collision between the sheep and an alien"""

        if self.stats.ship_left > 0:

            # Decrease ships count ( lives )
            self.stats.ship_left -= 1

            # Delete groups - aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and put it to the center
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            # Show mouse cursor
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        """Create a new bullet and add to group bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:  # limit bullet count
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and remove bullets on top of the screen"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Kill detection
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_aliens_bottom(self):
        """Detect alien-floor collision"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update all aliens' positions"""
        self._check_fleet_edges()
        self.aliens.update()

        # Alien - Ship collision detection
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Alien - Floor collision detection
        self._check_aliens_bottom()

    def _create_alien(self, x_position, y_position):
        """Create an alien and put it in a row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """Create alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # End of row: reset x and increase y
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """Check fleet edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move whole fleet down and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update image and new screen"""
        self.screen.fill(self.settings.bg_color)

        # for bullet in self.bullets.sprites():
        #     bullet.draw_bullet()
        self.bullets.draw(self.screen)

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        # Play button displays if game isn't active
        if not self.game_active:
            self.play_button.draw_button()

        # Show last drawed screen
        pygame.display.flip()

    def _check_events(self):
        """Listen keybord and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Launch a new game when play button is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

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
