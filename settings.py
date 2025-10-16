class Settings:
    """Game initial settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (14, 14, 14)
        self.ship_speed = 7

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliet settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # fleet_direction = 1 means to right, -1 means to left
        self.fleet_direction = 1
