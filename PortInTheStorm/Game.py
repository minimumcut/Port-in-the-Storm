# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame
from TowerEntity import CreateDefaultTowerEntity

class RegionData:
    def __init__(self):
        self.region_entities = []

class Game:
    def __init__(self, initial_level):
        print("Loading level " + initial_level.level_properties.level_name)
        initial_level.load()
        self.current_level = initial_level
        self.region_data = RegionData()
        self.all_sprites = pygame.sprite.Group()
        self.initialize_lighthouses()

    # This method iterates over the game map only once to create sprites based on the property 'sprite_type'
    # sprite_types can be:
    # - "lighthouse"
    # - "main"
    # - "ship"
    #
    # These sprite_types should be custom types added in the Tiled app (or the tmx editing app) for the tileset
    def initialize_lighthouses(self):
        game_map = self.current_level.loaded_sprite_map
        for layer in game_map.visible_layers:
            for x in range(0, 20):
                for y in range(0, 20):
                    properties = game_map.get_tile_properties(x, y, 0)
                    if properties:
                        if properties['sprite_type'] == "lighthouse":
                            towerEntity = CreateDefaultTowerEntity(x,y, self.region_data, True)
                            self.all_sprites.add(towerEntity.sprite)
                            continue
                        if properties['sprite_type'] == "main":
                            towerEntity = CreateDefaultTowerEntity(x,y, self.region_data, False)
                            self.all_sprites.add(towerEntity.sprite)
                            continue

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

        # render all the sprites
        self.all_sprites.draw(screen)

        pygame.display.flip()

    def GameTick(self):
        pass