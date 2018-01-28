# Import the pygame library and initialise the game engine
import pygame
import pytmx

from Constants import PIXEL_RESOLUTION
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

# these are copied by reference, so we should probs not use them, or if we do, deep copy them
# DEFAULT_LIGHT_RECIEVER_ANGLES = []
# DEFAULT_LIGHT_FORWARDER = [LightForwarder(4, 1.0)]
# DEFAULT_LIGHT_EMITTERS = [LightEmitter(4, 1.0)]

def CreateDefaultEmitterTower(x, y, region_data):
    towerType = TowerType([LightEmitter(4, 1.0)], [], [], 0)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    print("Ceated emitter at: " + str(x) + " " +  str(y))
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

def CreateDefaultForwarderTower(x, y, region_data):
    towerType = TowerType([], [LightForwarder(4, 1.0)], [], 0)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    print("Ceated forwarder at: " +  str(x) + " " +  str(y))
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

def CreateDefaultRecieverTower(x, y, region_data):
    towerType = TowerType([], [], [], 0, True)
    towerEntity = TowerEntity(x, y, None, towerType)
    region_data.region_entities.append(towerEntity)
    print("Ceated forwarder at: " +  str(x) + " " +  str(y))
    region_data.region_entities_grid[x][y] = towerEntity
    return towerEntity

def SetUpShipSprite(x,y, towerEntity):
    img = pygame.image.load('sprites/ship1.png')
    # @TODO anthonyluu: remove this after we switch to 64x64
    smaller_img = pygame.transform.scale(img, (PIXEL_RESOLUTION, PIXEL_RESOLUTION))

    towerEntity.sprite = Sprite(x=x, y=y, frames=[[smaller_img]])
    towerEntity.sprite.rect.x = x*PIXEL_RESOLUTION;
    towerEntity.sprite.rect.y = y*PIXEL_RESOLUTION;
    towerEntity.light_sprite = None;

def SetUpCloudSprite(x,y, towerEntity):
    towerEntity.tower_type.is_passable = False;
    img = pygame.image.load('sprites/fake_cloud.png')
    towerEntity.sprite = Sprite(x=x, y=y, frames=[[img]])
    towerEntity.sprite.rect.x = x*PIXEL_RESOLUTION;
    towerEntity.sprite.rect.y = y*PIXEL_RESOLUTION;
    towerEntity.light_sprite = None;

class TowerType:
    def __init__(self, light_emitters, light_forwarders, light_recievers, initial_rotation, is_passable=False):
        self.light_recievers = light_recievers
        self.light_emitters = light_emitters
        self.light_forwarders = light_forwarders
        self.initial_rotation = initial_rotation
        self.is_passable = is_passable
    def rotate_light(self, counter_clockwise=True):
        print("rotating light")
        #assuming that everytime this is called, it rotates by 45 degrees clockwise
        if counter_clockwise:
            dx = 1
        else:
            dx = -1
        for rcv in self.light_recievers:
            rcv.angle = (rcv.angle + dx) % 8
        for emitter in self.light_emitters:
            emitter.angle = (emitter.angle + dx) % 8
            print("emitter angle: ", emitter.angle)
        for fwd in self.light_forwarders:
            fwd.angle = (fwd.angle + dx) % 8
            print("fwd angle: ", fwd.angle)


class TowerEntity:
    def __init__(self, x, y, state, tower_type):
        # For cycle detection
        self.is_powered = False

        self.x = x
        self.y = y
        self.tower_type = tower_type
        # pos is placeholder
        self.sprite = Sprite(x=x, y=y, frames=[[pygame.image.load('sprites/tower.png')]])
        self.sprite.rect.x = x*PIXEL_RESOLUTION
        self.sprite.rect.y = y*PIXEL_RESOLUTION
        self.light_sprite = Sprite(x=x, y=y, frames=[[pygame.image.load('sprites/light.png')]], can_rotate=True)
        self.light_sprite.rect.x = x*PIXEL_RESOLUTION
        self.light_sprite.rect.y = y*PIXEL_RESOLUTION