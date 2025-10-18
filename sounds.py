import pygame

SOUNDS_PATH = 'sounds/'


class Sounds:
    """Sound control class"""

    def __init__(self, volume=0.5):
        self.hit_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}Boom2.wav")
        self.shoot_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}Shoot93.wav")
        self.level_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}Pickup40.wav")
        self.hurt_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}Hit29.wav")
        self.hit_sound.set_volume(volume)
        self.shoot_sound.set_volume(volume)

    def hit(self):
        self.hit_sound.play()

    def shoot(self):
        self.shoot_sound.play()

    def level_up(self):
        self.level_sound.play()

    def hurt(self):
        self.hurt_sound.play()
