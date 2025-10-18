class GameStats:
    """Track and manage stats for the game"""

    def __init__(self, ai_game):
        """Init Statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Initializes the statistics that change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
