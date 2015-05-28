# coding= utf-8

# Pygame and system modules
import sys
import pygame
from pygame.locals import *
from . import keyboard
from . import mouse

# Initializes pygame's modules
pygame.init()
    
"""A simple Window class, it's the primary Surface(from pygame).
All the other game's renderable objects will be drawn on it. """
class Window():
    #A class attribute in Python, this case is similar to Java statics
    screen = None
    
    """Initialize a Window (width x height)"""
    def __init__(self, width, height):
        # Input controllers
        Window.keyboard = keyboard.Keyboard()
        Window.mouse = mouse.Mouse()
        
        # Size
        self.width = width
        self.height = height

        # Pattern color
        self.color = [0,0,0]  # Black

        # Pattern Title
        self.title = "Title"

        # Time Control
        self.curr_time = 0  # current frame time
        self.last_time = 0  # last frame time 
        self.total_time = 0  # += curr-last(delta_time), update()

        # Creates the screen (pygame.Surface)
        # There are some useful flags (look pygame's docs)
        # It's like a static attribute in Java
        Window.screen = pygame.display.set_mode([self.width, self.height])
        # ? Why is it possible to do w.screen?

        # Sets pattern starting conditions
        self.set_background_color(self.color)
        self.set_title(self.title)

        # Updates the entire screen if no arguments are passed
        # Can be used to update portions of the screen (Rect list)
        pygame.display.update()

#------------------------TODO - VIDEO RESIZE METHODS----------------------
    """Not implemented yet - Sets the Window to Fullscreen"""
    # Unfortunately, it must save the old screen (buffer) and
    # blit (transfer, see pygame doc) to the new FSCREEN
    def set_fullscreen(self): pass
    # TODO

    """Not implemented yet - Disable the full display mode"""
    # Yeah.. guess what..
    def restoreScreen(self): pass
    # TODO

    """Not implemented yet - Sets the Window resolution"""
    # The same problem as fullscreen
    def set_resolution(self, width, height): pass
    # TODO
    
#-----------------------CONTROL METHODS---------------------------
    """Refreshes the Window - makes changes visible, AND updates the Time"""
    def update(self):
        pygame.display.update()  # refresh
        
        for event in pygame.event.get():  # necessary to not get errors
            if event.type==QUIT:
                self.close()
        self.last_time = self.curr_time  # set last frame time
        self.curr_time = pygame.time.get_ticks()  # since pygame.init()  
        self.total_time += (self.curr_time - self.last_time)  # == curr_time
        # curr_time should be the REAL current time, but in Python
        # the method returns the time in seconds.
        # And we DO WANT MILLIseconds :P
        # While REAL time is not necessary, yet..

    """Paints the screen - White - and update"""
    def clear(self):
        self.set_background_color([255,255,255])
        self.update()

    """
    Closes the Window and stops the program - throws an exception
    """
    def close(self):
        pygame.quit()
        sys.exit()
        
#---------------------GETTERS AND SETTERS METHODS-----------------
    """
    Changes background color - receives a vector [R, G, B] value
    Example: set_background_color([0,0,0]) -> black
    or set_background_color([255,255,255]) -> white
    """
    def set_background_color(self, RGB):
        self.color = RGB
        Window.screen.fill(self.color)
    # !Implement later possible strings values, such as:
    # "red","green","blue"..!

    """Gets the color attribute (background)"""
    def get_background_color(self):
        return self.color

    """Sets the title of the Window"""
    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    """Gets the title of the Window"""
    def get_title(self):
        return self.title

#----------------------TIME CONTROL METHODS--------------------------
        
    """Pause the program for an amount of time - milliseconds"""
    # Uses the processor to make delay accurate instead of
    # pygame.time.wait that SLEEPS the proccess
    def delay(self, time_ms):
        pygame.time.delay(time_ms)

    """
    Returns the time passed between
    the last and the current frame - SECONDS
    """
    def delta_time(self):
        return (self.curr_time - self.last_time)/1000.0

    """Returns the total time passed since the Window was created"""
    def time_elapsed(self):
        return self.total_time

#------------------------DRAW METHODS-------------------------------
    """
    Draw a text on the screen at X and Y co-ords, using [R, G, B] color
    [with the specified font,
           [with the specified size,
                   [Bold,
                         [Italic]]]]
    """
    def draw_text(self, text, x, y, size=12, color=(0,0,0),
                 font_name="Arial", bold=False, italic=False):
        # Creates a Font from the system fonts
        # SysFont(name, size, bold=False, italic=False) -> Font
        font = pygame.font.SysFont(font_name, size, bold, italic)

        # Creates a pygame.Surface with the text rendered on it
        # render(text, antialias, color, background=None)->Surface
        font_surface = font.render(text, True, color)
        # That's because pygame does NOT provide a way
        # to directly draw text on an existing Surface.
        # So you must use Font.render() -> Surface and BLIT
        
        # Finally! BLIT!
        self.screen.blit(font_surface, [x, y])

#---------------------CLASS METHODS--------------------------
    """Returns the drawing surface"""
    @classmethod
    def get_screen(cls):
        return cls.screen

    """Returns the keyboard input"""
    @classmethod
    def get_keyboard(cls):
        return cls.keyboard

    """Returns the mouse input"""
    @classmethod
    def get_mouse(cls):
        return cls.mouse
    


        
        
        
    
