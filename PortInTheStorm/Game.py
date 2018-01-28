import BeamRenderer
import Beam
import DialogParser
import pygame
import pytmx
import RenderPostFX
import TowerEntityRenderer

from Constants import PIXEL_RESOLUTION
from itertools import repeat
from pytmx import load_pygame
from TowerEntity import CreateDefaultEmitterTower, CreateDefaultForwarderTower, CreateDefaultRecieverTower, TowerType



pygame.font.init()

goose = pygame.image.load("sprites/char_goose_neutral.png")

DIALOGUE_BOX_RECT = (80, 500, 1120, 150)
TEXT_BOX_RECT = (120, 520, 1000, 110)
LEFT_CHARACTER_SPRITE_POS = (120, 300) 
RIGHT_CHARACTER_SPRITE_POS = (800, 300) 

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RegionData:
    def __init__(self):
        self.region_entities_grid = []
        self.region_entities = []
        self.region_beams = []
        self.main_tower = None
        self.light_on = False
        self.ships = []

class DialogData:
    def __init__(self):
        self.current_left_sprite = None
        self.current_right_sprite = None
        self.show_dialogue_box = False
        self.current_dialogue = "HA"

class Game:
    def __init__(self, initial_level):
        print("Loading level " + initial_level.level_properties.level_name)
        initial_level.load()
        self.current_level = initial_level
        self.region_data = RegionData()
        # self.region_data.region_entities_grid = list(repeat(None, self.current_level.height))

        # for i in range(0, self.current_level.height):
        #     self.region_data.region_entities_grid[i] = list(repeat(None, self.current_level.width))
        
        self.region_data.region_entities_grid = [[None for x in range(self.current_level.width)] for y in range(self.current_level.height)]

        self.all_sprites = pygame.sprite.Group()
        self.initialize_lighthouses()
        # self.UpdateTowerStates()
        self.dialog_data = DialogData()

    def TransitionToLevel(next_level):
        print("Loading level " + next_level.level_properties.level_name)
        self.current_level = next_level
        self.region_data = RegionData()
        self.all_sprites = pygame.sprite.Group()
        self.initialize_lighthouses()
        self.UpdateTowerStates()
        self.dialog_data = DialogData()

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
                            towerEntity = CreateDefaultForwarderTower(x, y, self.region_data)
                            self.all_sprites.add(towerEntity.sprite)
                            self.all_sprites.add(towerEntity.light_sprite)
                            continue
                        if properties['sprite_type'] == "main":
                            towerEntity = CreateDefaultEmitterTower(x, y, self.region_data)
                            self.region_data.main_tower = towerEntity
                            self.all_sprites.add(towerEntity.sprite)
                            self.all_sprites.add(towerEntity.light_sprite)
                            continue
                        if properties['sprite_type'] == "ship":
                            towerEntity = CreateDefaultRecieverTower(x, y, self.region_data)
                            self.all_sprites.add(towerEntity.sprite)
                            self.region_data.ships.append(towerEntity)
                            # no light sprite
                            continue
    def set_dialogue():
        pass

    def hide_dialogue_box():
        pass

    def RotateClickedSprites(self, clicked_sprites):
        # print("rotating clicked sprites", len(clicked_sprites))
        for sprite in clicked_sprites:
            # rotates the sprite, and also updates the tower type's to point in the right direction
            if sprite.can_rotate:
                print("a sprite will rotate at ", sprite.x, sprite.y)
                sprite.rotate_frames(45)
                # import pdb; pdb.set_trace()
                self.region_data.region_entities_grid[sprite.x][sprite.y].tower_type.rotate_light()

    def render_dialogue_box(self, surface):
        if not self.dialog_data.show_dialogue_box:
            return
        pygame.draw.rect(surface, (255,255,255), DIALOGUE_BOX_RECT)

        text = self.dialog_data.current_dialogue
        color = (0, 0, 0)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(TEXT_BOX_RECT)
        y = rect.top
        lineSpacing = -2

        fontHeight = font.size("Comic Sans MS")[1]
        while text:
            i = 1
            if y + fontHeight > rect.bottom:
                break
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            image = font.render(text[:i], False, color)
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            text = text[i:]
        return text

    def TurnOffLights(self):
        # removing the beams and cleaning up the tower
        self.region_data.region_beams = []
        self.region_data.light_on = False

    def ToggleLight(self):
        print("space pressed")
        if self.region_data.light_on:
            # its on, turning it off
            self.TurnOffLights()
        else:
            # its off, turning it on
            # adding back the first emitter, and then updating tower states
            self.UpdateTowerStates()
            self.region_data.light_on = True
            self.CheckIfAllShipsPowered()


    def render_character_sprite(self, surface):
        if self.dialog_data.current_left_sprite != None:
           surface.blit(goose, LEFT_CHARACTER_SPRITE_POS)

        if self.dialog_data.current_right_sprite != None:
           surface.blit(goose, Right_CHARACTER_SPRITE_POS)


    # Returns false
    def HandleInputEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_q or event.key == pygame.K_SPACE:
                    self.ToggleLight()
                if event.key == pygame.K_w:
                    self.dialog_data.show_dialogue_box = not self.dialog_data.show_dialogue_box
                if event.key == pygame.K_a:
                    print("w pressed")
            if event.type == pygame.MOUSEBUTTONUP:
                # when rotating, turn off lights
                self.TurnOffLights()
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in self.all_sprites if s.rect.collidepoint(pos) and s.can_rotate]
                self.RotateClickedSprites(clicked_sprites)
        return True

    def Render(self, screen):
        game_map = self.current_level.loaded_sprite_map
        for layer in game_map.visible_layers:
                for x in range(0, 20):
                    for y in range(0, 20):
                        pygame_surface = game_map.get_tile_image(x, y, 0)
                        screen.blit(pygame_surface, (PIXEL_RESOLUTION*x, PIXEL_RESOLUTION*y))


        TowerEntityRenderer.RenderTowers(screen, self.region_data.region_entities)
        BeamRenderer.RenderBeams(screen, self.region_data.region_beams)

        RenderPostFX.RenderVignette(screen)
        
        self.render_dialogue_box(screen)
        self.render_character_sprite(screen)

        pygame.display.flip()


    def CheckIfAllShipsPowered(self):
        for ship in self.region_data.ships:
            if not ship.is_powered:
                print("ships arent fully powered yet")
                return False
        print("ships are powered!!! Done level")
        # TODO: do this when done TransitionToLevel()
        return True

    def UpdateTowerStates(self):
        # fuck it O(N^3) baby
        for tower in self.region_data.region_entities:
            tower.is_powered = False

        self.region_data.region_beams = [] 

        for fuck_you in self.region_data.region_entities:
            self.DetermineTowersBeamIntersect(self.region_data.region_entities)

    def GameTick(self):
        pass

    def GetTowerFromRegionGrid(self, x, y):
        if x >= 0 and x < self.current_level.width and y >= 0 and y < self.current_level.height:
            return self.region_data.region_entities_grid[x][y]
        return None
    
    def OnIntersect(self, source_tower, destination, intersect_angle):
        dest_tower = self.GetTowerFromRegionGrid(destination.x, destination.y)
        if(dest_tower != None):
            dest_tower.is_powered = True
        
        # Create the beam
        beam_type = Beam.BeamType((255,255,255), 5, 5, 5) 
        new_beam = Beam.Beam(source_tower.x, source_tower.y, destination.x, destination.y, beam_type)
        self.region_data.region_beams.append(new_beam)

    def DetermineTowersBeamIntersect(self, towers):
        for tower in towers:
            x = tower.x
            y = tower.y
            origin = Coord(x, y)
            emitter_list = tower.tower_type.light_emitters
            for emitter in emitter_list:
                
                intersect = self.DetermineBeamIntersect(x, y, emitter.angle)
                self.OnIntersect(tower, intersect, emitter.angle)
                
            if tower.is_powered:
                forwarder_list = tower.tower_type.light_forwarders
                for forwarder in forwarder_list:
                    intersect = self.DetermineBeamIntersect(x, y, forwarder.angle)
                    self.OnIntersect(tower, intersect, forwarder.angle)
            
    def DetermineBeamIntersect(self, x, y, direction):
        dx = 0
        dy = 0

        # lol
        if direction == 0:
            dy = 1
        elif direction == 1:
            dx = 1
            dy = 1
        elif direction == 2:
            dx = 1
        elif direction == 3:
            dx = 1
            dy = -1
        elif direction == 4:
            dy = -1
        elif direction == 5:
            dx = -1
            dy = -1
        elif direction == 6:
            dx = -1
        elif direction == 7:
            dx = -1
            dy = 1
        
        #print("HI")
        #print(self.current_level.width)
        #print(self.current_level.height)
        print(len(self.region_data.region_entities_grid))

        x = x + dx
        y = y + dy
        
        while x >= 0 and x < self.current_level.width and y >= 0 and y < self.current_level.height:
            if self.region_data.region_entities_grid[x][y] != None:
                if self.region_data.region_entities_grid[x][y].tower_type.is_passable:
                    self.region_data.region_entities_grid[x][y].is_powered = True
                else:
                    print("Encountered collision at: " + str(x) + " " + str(y))
                    return Coord(x,y)
        
            x = x + dx
            y = y + dy

        return Coord(x,y)
