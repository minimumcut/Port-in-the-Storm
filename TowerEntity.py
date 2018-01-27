# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame

class TowerEntity:
    def __init__(self, x, y, initial_rotation):
        self.x = x
        self.y = y
        self.initial_rotation = initial_rotation
