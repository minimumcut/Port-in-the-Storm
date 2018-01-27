# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame

class TowerType:
    def __init__(self, enabled_light_reciever_angles, enabled_light_transmittor_angles, initial_rotation):
        self.enabled_light_reciever_angles = enabled_light_reciever_angles
        self.enabled_light_transmittor_angles = enabled_light_transmittor_angles
        self.initial_rotation = initial_rotation
        
class TowerEntity:
    def __init__(self, x, y, towerType):
        self.x = x
        self.y = y
        self.towerType = towerType

