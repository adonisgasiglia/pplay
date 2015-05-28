# coding= utf-8

# Modules
import sys
import time
import pygame
from . import window
from . import animation
from pygame.locals import *

# Initializes pygame's modules
pygame.init()

"""Sprite é uma animação que pode ser movida por input, é o "ator" do jogo"""
class Sprite(animation.Animation):
    """
    Caso seja dado apenas o nome da imagem, será criada uma Animation
    com 1 frame apenas.
    """
    def __init__(self, image_file, frames=1):
        # Parent's constructor must be first-called
        animation.Animation.__init__(self, image_file, frames)

    """Permite a movimentação com o teclado no eixo X"""
    def move_key_x(self, speed):
        if(window.Window.get_keyboard().key_pressed("left")):
            self.set_position(self.x - speed, self.y)
            
        if(window.Window.get_keyboard().key_pressed("right")):
            self.set_position(self.x + speed, self.y)

    """Permite a movimentação com o telado no eixo Y"""
    def move_key_y(self, speed):
        if(window.Window.get_keyboard().key_pressed("up")):
            self.set_position(self.x, self.y - speed)
            
        if(window.Window.get_keyboard().key_pressed("down")):
            self.set_position(self.x, self.y + speed)

    """Move o Sprite no eixo X (sem input)"""
    def move_x(self, speed):
        self.x += speed
        self.set_position(self.x, self.y)

    """Move o Sprite no eixo Y (sem input)"""
    def move_y(self, speed):
        self.y += speed
        self.set_position(self.x, self.y)
            
