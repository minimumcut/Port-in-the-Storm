# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame

def LoadLevel(Level):
    level.loaded_sprite_map = load_pygame("test.tmx")
    level.loaded = true

class LevelProperties:
    def __init__(self, level_name, level_number):
        self.level_name = level_name
        self.level_number = level_number 

class Level:
    def __init__(self, level_properties, width, height, tower_list, sprite_map):
        self.color = color
        self.width = width 
        self.height = height
        self.tower_list = tower_list
        self.sprite_map = sprite_map
        self.level_properties = level_properties 

    def draw_base_layer(self, pygame_screen):
        if not loaded:
            raise AssertionError()

        for layer in gameMap.visible_layers:
            for x in range(0, width):
                for y in range(0, height):
                    pygame_surface = gameMap.get_tile_image(x, y, 0)
                    screen.blit(pygame_surface, (32*x, 32*y))

    def draw_towers(self, pygame_screen):
        for tower in tower_list:
            tower_type = tower.tower_type
            # screen.blit(pygame_surface, (32*x, 32*y))