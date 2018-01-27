# Import the pygame library and initialise the game engine
import pygame
import pytmx
import RenderPostFX
import BeamRenderer
import Beam
from pytmx import load_pygame

class RegionData:
    def __init__(self):
        self.region_entities = []

class Game:
    def __init__(self, initial_level):
        print("Loading level " + initial_level.level_properties.level_name)
        initial_level.load()
        self.current_level = initial_level
        self.region_data = RegionData()        

    # Returns false 
    def HandleInputEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_w:
                    print("w pressed")
                if event.key == pygame.K_a:
                    print("w pressed")
        return True

    def Render(self, screen):
        game_map = self.current_level.loaded_sprite_map
        for layer in game_map.visible_layers:
                for x in range(0, 20):
                    for y in range(0, 20):
                        pygame_surface = game_map.get_tile_image(x, y, 0)
                        screen.blit(pygame_surface, (32*x, 32*y))
                        
        RenderPostFX.RenderVignette(screen)
        
        # Test rendering beam
        beamProps = Beam.BeamType((255,255,255), 3, 10, 10)
        beam = Beam.Beam(0, 0, 250, 250, beamProps)
        BeamRenderer.RenderBeams(screen, [beam])

        pygame.display.flip()

    def GameTick(self):
        pass