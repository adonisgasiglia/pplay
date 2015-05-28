# coding= utf-8

import pygame
import pygame.mixer

# Initizalizes pygame's modules
pygame.init()
"""Sound é uma classe de controle dos sons do jogo - efeitos, música"""
class Sound():
    """ATENÇÃO! O arquivo passado deve ser .OGG!!! Se não pode gerar problemas."""
    def __init__(self, sound_file):
        self.loop = False
        self.sound_file = sound_file
        self.volume = 50
        self.sound = self.load(sound_file)
        self.set_volume(self.volume)

        # To reduce audio delay
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

    def load(self, sound_file):
        if(pygame.mixer):
            return pygame.mixer.Sound(sound_file)

    """Value deve ser um valor entre 0 e 100"""
    def set_volume(self, value):
        if(value >= 100):
            value = 100
        if(value <= 0):
            value = 0

        self.volume = value
        self.sound.set_volume(value/100)

    def increase_volume(self, value):
        self.set_volume(self.volume + value)

    def decrease_volume(self, value):
        self.set_volume(self.volume - value)

    def is_playing(self):
        if(pygame.mixer.get_busy()):
            return True
        else:
            return False

    def pause(self):
        pygame.mixer.pause()

    def unpause(self):
        pygame.mixer.unpause()

    def play(self):
        if(self.loop):
            self.sound.play(-1)
        else:
            self.sound.play()

    def stop(self):
        self.sound.stop()

    def set_repeat(self, repeat):
        self.loop = repeat

    def fadeout(self, time_ms):
       self.sound.fadeout(time_ms)


