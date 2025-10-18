import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class ScoreBoard:
    """Class for displaying game information"""

    def __init__(self, ai_game: "AlienInvasion"):
        """Initialize score-tracking attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for displaying the score
        self.text_color = (200, 200, 200)
        # self.font = pygame.font.Font("./fonts/PixelifySans-Regular.ttf", 48)
        self.font = pygame.font.SysFont("Monospace", 50)

        self.prep_score()

    def prep_score(self):
        """Transform current score to graphic image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        # score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # Render the score at the top-right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Render the score"""
        self.screen.blit(self.score_image, self.score_rect)
