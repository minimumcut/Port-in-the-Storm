# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame
from Sprite import Sprite

DEFAULT_LIGHT_RECIEVER_ANGLES = [False, True, True, True, True, True, True, True]
DEFAULT_LIGHT_TRANSMITTER_ANGLES = [True, False, False, False, False, False, False, False]

def CreateDefaultTowerEntity(x, y, region_data, is_reciever):
    # creates a default tower and appends it to region_data
    towerType = TowerType(DEFAULT_LIGHT_RECIEVER_ANGLES, DEFAULT_LIGHT_TRANSMITTER_ANGLES, 0, is_reciever)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    return towerEntity

class TowerType:
    def __init__(self, enabled_light_reciever_angles, enabled_light_transmittor_angles, initial_rotation, is_reciever):
        self.enabled_light_reciever_angles = enabled_light_reciever_angles
        self.enabled_light_transmittor_angles = enabled_light_transmittor_angles
        self.initial_rotation = initial_rotation
        self.is_reciever = is_reciever

class TowerEntity:
    def __init__(self, x, y, state, tower_type):
        self.x = x
        self.y = y
        self.tower_type = tower_type
        # pos is placeholder
        self.sprite = Sprite(pos=0, angle=0, frames=[[pygame.image.load('sprites/whitesprite.png')]])
        self.sprite.rect.x = x*32
        self.sprite.rect.y = y*32