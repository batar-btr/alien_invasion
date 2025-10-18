class Settings:
    """Game initial settings"""

    def __init__(self):
        # Init static settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (14, 14, 14)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # Game speed increase rate
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.bullet_speed = 7.0
        self.ship_speed = 7
        self.alien_speed = 1.0
        # fleet_direction = 1 means to right, -1 means to left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
