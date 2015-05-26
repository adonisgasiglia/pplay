# Pygame and system modules
import sys
import pygame
from pygame.locals import *
from . import window
from . import gameobject

# Initializes pygame's modules
pygame.init()
        
"""GameImage is the base class to deal with images"""
class GameImage(gameobject.GameObject):
    """
    Creates a GameImage from the specified file.
    The width and height are obtained based on the image file.
    """
    def __init__(self, image_file):
        # Parent constructor must be called first
        gameobject.GameObject.__init__(self)
        
        # Loads image from the source
        self.file_name = image_file
        self.image = pygame.image.load(image_file)

        # Size
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

        

    """Draws the image on the screen"""
    def draw(self):
        # A instance of the Window screen
        # Window object must've been instatiated
        # draw_rect is necessary to readjust the image position given .x and .y
        draw_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        window.Window.get_screen().blit(self.image, draw_rect)

    """Sets the (X,Y) image position on the screen"""
    def set_position(self, x, y):
        self.x = x
        self.y = y
