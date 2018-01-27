# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame
from Sprite import Sprite

class LightReciever:
    def __init__(self, angle, req_input):
         self.angle = angle
         self.req_input = req_input

class LightForwarder:
    def __init__(self, angle, amplification):
         self.angle = angle
         self.amplification = amplification

class LightEmitter:
    def __init__(self, angle, out):
         self.angle = angle
         self.out = out

DEFAULT_LIGHT_RECIEVER_ANGLES = []
DEFAULT_LIGHT_FORWARDER = [LightForwarder(1, 1.0), LightForwarder(2, 1.0), LightForwarder(3, 1.0),
                           LightForwarder(4, 1.0), LightForwarder(5, 1.0), LightForwarder(6, 1.0),
                           LightForwarder(7, 1.0), LightForwarder(8, 1.0)]
DEFAULT_LIGHT_EMITTERS = [LightEmitter(0, 1.0)]

def CreateDefaultEmitterTower(x, y, region_data):
    towerType = TowerType(DEFAULT_LIGHT_EMITTERS, [], [], 0)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

def CreateDefaultForwarderTower(x, y, region_data):
    towerType = TowerType([], DEFAULT_LIGHT_FORWARDER, [], 0)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

def CreateDefaultRecieverTower(x, y, region_data):
    towerType = TowerType([], [], DEFAULT_LIGHT_RECIEVER_ANGLES, 0)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

class TowerType:
    def __init__(self, light_recievers, light_emitters, light_forwarders, initial_rotation):
        self.light_recievers = light_recievers
        self.light_emitters = light_emitters
        self.light_forwarders = light_forwarders
        self.initial_rotation = initial_rotation

class TowerEntity:
    def __init__(self, x, y, state, tower_type):
        # For cycle detection
        self.is_powered = False

        self.x = x
        self.y = y
        self.tower_type = tower_type
        # pos is placeholder
        self.sprite = Sprite(pos=0, frames=[[pygame.image.load('sprites/whitesprite.png')]])
        self.sprite.rect.x = x*32
        self.sprite.rect.y = y*32