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
from TowerEntity import CreateDefaultEmitterTower, CreateDefaultForwarderTower, CreateDefaultRecieverTower, TowerType, SetUpShipSprite, SetUpCloudSprite
from Sprite import Sprite as CustomSprite

pygame.font.init()

DIALOGUE_BOX_RECT = (80, 500, 800, 150)
TEXT_BOX_RECT = (120, 520, 720, 110)
LEFT_CHARACTER_SPRITE_POS = (50, 300) 
RIGHT_CHARACTER_SPRITE_POS = (580, 300) 
from enum import Enum

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
        self.light_on = True
        self.ships = []
        self.victory = False
        self.transitioning = False
        self.transition_countdown = 30
        self.beam_countdown = 10
        self.water_frames = [ \
            pygame.image.load('sprites/water_tiles/water1.png'), \
            pygame.image.load('sprites/water_tiles/water2.png'), \
            pygame.image.load('sprites/water_tiles/water3.png'), \
            pygame.image.load('sprites/water_tiles/water4.png') \
        ]

class DialogData:
    def __init__(self):
        self.dialog_cmd_list = None
        self.current_left_sprite = None
        self.current_right_sprite = None
        self.show_dialogue_box = False
        self.current_dialogue = "HA"

class Game:
    def __init__(self, level_list):
        self.level_list = level_list
        self.TransitionLevel()

    def TransitionLevel(self):
        if(self.level_list == 0):
            print("You win!")

        next_level = self.level_list[0]
        self.level_list = self.level_list[1:]
        next_level.load()

        self.current_level = next_level
        self.region_data = RegionData()
        self.region_data.region_entities_grid = [[None for x in range(self.current_level.height)] for y in range(self.current_level.width)]
        self.bg_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.initialize_lighthouses()
        self.dialog_data = DialogData()
        self.dialog_data.dialog_cmd_list = self.current_level.loaded_pre_level_dialog
        if self.dialog_data.dialog_cmd_list != None:
            self.advance_dialog() 
        self.UpdateTowerStates()

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
            for x in range(0, 14):
                for y in range(0, 10):
                    wf = [ \
                        pygame.image.load('sprites/water_tiles/water1.png'), \
                        pygame.image.load('sprites/water_tiles/water2.png'), \
                        pygame.image.load('sprites/water_tiles/water3.png'), \
                        pygame.image.load('sprites/water_tiles/water4.png'), \
                        pygame.image.load('sprites/water_tiles/water5.png'), \
                        pygame.image.load('sprites/water_tiles/water6.png'), \
                        pygame.image.load('sprites/water_tiles/water7.png'), \
                        pygame.image.load('sprites/water_tiles/water8.png'), \
                        pygame.image.load('sprites/water_tiles/water9.png'), \
                        pygame.image.load('sprites/water_tiles/water10.png'), \
                    ]
                    bg_sprite = CustomSprite(x, y, frames=[wf])
                    bg_sprite.rect.x = x*PIXEL_RESOLUTION
                    bg_sprite.rect.y = y*PIXEL_RESOLUTION
                    self.bg_sprites.add(bg_sprite)
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
                            # set up ship sprites
                            SetUpShipSprite(x,y,towerEntity)
                            self.all_sprites.add(towerEntity.sprite)
                            self.region_data.ships.append(towerEntity)
                            continue
                        if properties['sprite_type'] == "cloud":
                            towerEntity = CreateDefaultRecieverTower(x, y, self.region_data)
                            SetUpCloudSprite(x,y,towerEntity)
                            self.all_sprites.add(towerEntity.sprite)
                            continue


    def dialog_finshed(self):
        self.hide_dialogue_box()
        if self.region_data.victory:
            self.region_data.transitioning = True
    
    def advance_dialog(self):
        if(len(self.dialog_data.dialog_cmd_list) == 0):
            self.dialog_finshed()
            return

        dialog = self.dialog_data.dialog_cmd_list[0]
        self.dialog_data.dialog_cmd_list = self.dialog_data.dialog_cmd_list[1:]

        #import pdb; pdb.set_trace()
        if dialog.type == "Character":
            l_char=pygame.image.load(dialog.left_character)
            r_char=pygame.image.load(dialog.right_character)
            self.set_character(l_char, r_char)
            self.advance_dialog()

        if dialog.type == "Dialog":
            self.set_dialogue(dialog.text)

    def set_character(self, left_character, right_character):
        self.dialog_data.current_left_sprite = left_character
        self.dialog_data.current_right_sprite = right_character

    def set_dialogue(self, text):
        self.dialog_data.show_dialogue_box = True
        self.dialog_data.current_dialogue = text

    def hide_dialogue_box(self):
        self.dialog_data.show_dialogue_box = False
        self.dialog_data.current_left_sprite = None
        self.dialog_data.current_right_sprite = None

    def RotateClickedSprites(self, clicked_sprites, counter_clockwise=True):
        if counter_clockwise:
            angle = 45
        else:
            angle = -45
        for sprite in clicked_sprites:
            # rotates the sprite, and also updates the tower type's to point in the right direction
            if sprite.can_rotate:
                sprite.rotate_frames(angle)
                # import pdb; pdb.set_trace()
                self.region_data.region_entities_grid[sprite.x][sprite.y].tower_type.rotate_light(counter_clockwise)

    def render_dialogue_box(self, surface):
        if not self.dialog_data.show_dialogue_box:
            return
        pygame.draw.rect(surface, (255,255,255), DIALOGUE_BOX_RECT)

        text = self.dialog_data.current_dialogue
        color = (0, 0, 0)
        font = pygame.font.SysFont('Comic Sans MS', 24)
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
        if self.region_data.light_on:
            # its on, turning it off
            self.TurnOffLights()
        else:
            # its off, turning it on
            # adding back the first emitter, and then updating tower states
            self.UpdateTowerStates()
            self.region_data.light_on = True

    def render_character_sprite(self, surface):
        if self.dialog_data.show_dialogue_box:
            RenderPostFX.RenderScreenMask(surface)
        if self.dialog_data.show_dialogue_box and self.dialog_data.current_left_sprite != None:
           surface.blit(self.dialog_data.current_left_sprite, LEFT_CHARACTER_SPRITE_POS)

        if self.dialog_data.show_dialogue_box and self.dialog_data.current_right_sprite != None:
           surface.blit(self.dialog_data.current_right_sprite, RIGHT_CHARACTER_SPRITE_POS)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.dialog_data.show_dialogue_box:
                    self.advance_dialog()
                else:
                    # when rotating, turn off lights
                    #self.TurnOffLights()
                    pos = pygame.mouse.get_pos()
                    clicked_sprites = [s for s in self.all_sprites if s.rect.collidepoint(pos) and s.can_rotate]
                    # event.button == 1 left click
                    if event.button == 1:
                        self.RotateClickedSprites(clicked_sprites, False)
                        # event.button == 3 right click
                    elif event.button == 3:
                        self.RotateClickedSprites(clicked_sprites, True)
                    self.UpdateTowerStates()
        return True

    def Render(self, screen):
        game_map = self.current_level.loaded_sprite_map
        for layer in game_map.visible_layers:
                for x in range(0, 14):
                    for y in range(0, 10):
                        pygame_surface = game_map.get_tile_image(x, y, 0)
                        screen.blit(pygame_surface, (PIXEL_RESOLUTION*x, PIXEL_RESOLUTION*y))

        self.bg_sprites.draw(screen)

        TowerEntityRenderer.RenderTowers(screen, self.region_data.region_entities)
        BeamRenderer.RenderBeams(screen, self.region_data.region_beams)

        RenderPostFX.RenderVignette(screen)
        RenderPostFX.RenderRain(screen)

        self.render_character_sprite(screen)        
        self.render_dialogue_box(screen)

        if self.region_data.transitioning:
            RenderPostFX.RenderOpaqueScreenMask(screen)

        pygame.display.flip()

    def WinLevel(self):
        self.region_data.victory = True
        self.dialog_data.dialog_cmd_list = self.current_level.loaded_post_level_dialog
        if self.dialog_data.dialog_cmd_list != None:
            self.advance_dialog() 
        else:
            self.dialog_finshed()
            

    def CheckIfAllShipsPowered(self):
        for ship in self.region_data.ships:
            if not ship.is_powered:
                self.region_data.beam_countdown = 15
                #import pdb; pdb.set_trace()
                return False
        if self.region_data.beam_countdown == 0:
            #import pdb; pdb.set_trace()
            self.WinLevel()
            return True
        else:
            self.region_data.beam_countdown = self.region_data.beam_countdown - 1

    def UpdateTowerStates(self):
        # fuck it O(N^3) baby
        for tower in self.region_data.region_entities:
            tower.is_powered = False

        self.region_data.region_beams = [] 

        for fuck_you in self.region_data.region_entities:
            self.DetermineTowersBeamIntersect(self.region_data.region_entities)        

    def GameTick(self):
        if self.region_data.transitioning:
            self.region_data.transition_countdown = self.region_data.transition_countdown - 1
            if(self.region_data.transition_countdown <= 0):
                self.TransitionLevel() 
        if not self.region_data.victory:
            self.CheckIfAllShipsPowered()

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
        
        x = x + dx
        y = y + dy
        
        while x >= 0 and x < self.current_level.width and y >= 0 and y < self.current_level.height:
            if self.region_data.region_entities_grid[x][y] != None:
                if self.region_data.region_entities_grid[x][y].tower_type.is_passable:
                    self.region_data.region_entities_grid[x][y].is_powered = True
                else:
                    return Coord(x,y)
        
            x = x + dx
            y = y + dy

        return Coord(x,y)
