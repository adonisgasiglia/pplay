# coding= utf-8

# Pygame and System Modules
import sys
import time
import pygame
from . import window
from . import gameimage
from pygame.locals import *

# Initializes pygame's modules
pygame.init()

"""An Animation class for frame-control."""
class Animation(gameimage.GameImage):
    """
    Creates an Animation that is composed by N frames.
    The method set_sequence_time must be called right after.
    Must note that the nnumber of frames will be automatically
    computated: if the image has 100px width and total_frames = 10,
    each frame will have 10px width.
    """
    def __init__(self, image_file, total_frames, loop=True):
        # Parent's constructor must be first-called
        gameimage.GameImage.__init__(self, image_file)

        # A Cast to force it to be a float division
        self.width = self.width/float(total_frames)  # The width of each frame
        self.height = self.height

        # Playing Control
        self.playing = True
        self.drawable = True
        self.loop = loop

        self.total_frames = total_frames
        self.initial_frame = 0
        self.curr_frame = 0
        self.final_frame = total_frames

        # The duration of each frame
        self.frame_duration = []
        self.total_duration = 0

        # The actual time in ms
        self.last_time = int(round(time.time() * 1000))

        self.set_sequence(0, self.total_frames, self.loop)

        
    #-----------------------SEQUENCE SETTERS-----------------
    """
    Sets some aspects of the sequence, init/final frame, loop..
    """
    def set_sequence(self, initial_frame, final_frame, loop=True):
        self.set_initial_frame(initial_frame)
        self.set_curr_frame(initial_frame)
        self.set_final_frame(final_frame)
        self.set_loop(loop)

    """Defines each frame duration and the sequence (time / total_frames)."""
    def set_sequence_time(self, initial_frame, final_frame,
                          total_duration, loop=True):
        self.set_sequence(initial_frame, final_frame, loop)
        time_ms = int(round(total_duration / float(final_frame - initial_frame + 1)))
        for x in range(initial_frame, final_frame):
            self.frame_duration.append(total_duration)

    """Sets the time for all frames."""
    def set_total_duration(self, time_ms):
        time_frame = float(time_ms) / self.total_frames
        self.total_duration = time_frame * self.total_frames
        for x in range(0, self.total_frames):
            self.frame_duration.append(time_frame)

    #-----------------------DRAW&UPDATE METHODS--------------------
    """Method responsible for performing the change of frames."""
    def update(self):
        if(self.playing):
            time_ms = int(round(time.time() * 1000)) #gets the curr time in ms
            if((time_ms - self.last_time > self.frame_duration[self.curr_frame])
               and (self.final_frame != 0)):
                self.curr_frame += 1
                self.last_time = time_ms
            if((self.curr_frame == self.final_frame) and (self.loop)):
                self.curr_frame = self.initial_frame
            else:
                if((not self.loop) and (self.curr_frame + 1 >= self.final_frame)):
                    self.curr_frame = self.final_frame - 1
                    self.playing = False
            
    """Draws the current frame on the screen."""
    def draw(self):
        if(self.drawable):
            # Clips the frame (rect on the image)
            clip_rect = pygame.Rect(self.curr_frame*self.width,
                                    0,
                                    self.width,
                                    self.height
                                    )

            # Updates the pygame rect based on new positions values
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

            # Blits the image with the rect and clip_rect clipped
            window.Window.get_screen().blit(self.image, self.rect, area=clip_rect)
        
    
    #----------------------PLAYING CONTROL METHODS----------------------
    """Stops execution and puts the initial frame as the current frame."""
    def stop(self):
        self.curr_frame = self.initial_frame
        self.playing = False

    """Method responsible for starting the execution of the animation."""
    def play(self):
        self.playing = True

    """Method responsible fo pausing the Animation."""
    def pause(self):
        self.playing = False
        
    """Returns true if the Animation is being executed."""
    def is_playing(self):
        return self.playing

    """Returns if the Animation is looping."""
    def is_looping(self):
        return self.loop

    """Sets if the Animation will loop or not."""
    def set_loop(self, loop):
        self.loop = loop

    """Does not allow the Animation to be drawn on the screen."""
    def hide(self):
        self.drawable = False

    """Allows the Animation to be drawn on the screen."""
    def unhide(self):
        self.drawable = True

    #----------------GETTER&SETTER METHODS----------------       
    """Gets the total duration - sum of all time frames."""
    def get_total_duration(self):
        return self.total_duration
    
    """Sets the initial frame of the sequence of frames."""
    def set_initial_frame(self, frame):
        self.initial_frame = frame

    """Returns the initial frame of the sequence."""
    def get_initial_frame(self):
        return self.initial_frame

    """Sets the final frame of the sequence of frames."""
    def set_final_frame(self, frame):
        self.final_frame = frame

    """Returns the number of final frame of the sequence."""
    def get_final_frame(self):
        return self.final_frame

    """Sets the current frame that will be drawn."""
    def set_curr_frame(self, frame):
        self.curr_frame = frame

    """Gets the current frame that will be drawn."""
    def get_curr_frame(self):
        return self.curr_frame
    
