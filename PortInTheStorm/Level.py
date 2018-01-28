import DialogParser
import pygame
import pytmx

from Constants import PIXEL_RESOLUTION
from pytmx import load_pygame

class LevelProperties:
    def __init__(self, level_name, level_number):
        self.level_name = level_name
        self.level_number = level_number 

class Level:
    def __init__(self, level_properties, width, height, tower_list, sprite_map, pre_level_dialog=None, post_level_dialog=None):
        self.width = width 
        self.height = height
        self.tower_list = tower_list
        self.sprite_map = sprite_map
        self.level_properties = level_properties 
        self.pre_level_dialog = pre_level_dialog
        self.post_level_dialog = post_level_dialog

    def draw_base_layer(self, pygame_screen):
        if not loaded:
            raise AssertionError()

        for layer in gameMap.visible_layers:
            for x in range(0, width):
                for y in range(0, height):
                    pygame_surface = loaded_sprite_map.get_tile_image(x, y, 0)
                    screen.blit(pygame_surface, (PIXEL_RESOLUTION*x, PIXEL_RESOLUTION*y))
                    
    def load(self):
        self.loaded_sprite_map = load_pygame(self.sprite_map)
        self.loaded = True
        if self.post_level_dialog != None:
            self.loaded_post_level_dialog = DialogParser.Parse(self.post_level_dialog)
        if self.pre_level_dialog != None:
            self.loaded_pre_level_dialog = DialogParser.Parse(self.pre_level_dialog)
            