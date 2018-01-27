# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame

class BeamType:
    # Color, width and intensity are visual parameters for the beam
    # while the beam is a gameplay parameter 
    def __init__(self, color, width, intensity, strength):
        self.color = color
        self.width = width 
        self.intensity = intensity
        self.strength = strength

class Beam:
    def __init__(self, x_origin, y_origin, x_dest, y_dest, beamType):
        self.x = x_origin
        self.y = y_origin
        self.x_dest = y_dest
        self.y_dest = y_dest
        self.beamType = beamType
        