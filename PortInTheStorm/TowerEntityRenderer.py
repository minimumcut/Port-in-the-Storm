import pygame
import Beam

def RenderTowers(screen, tower_entities):
    sprite_list = pygame.sprite.LayeredUpdates()

    for tower_entity in tower_entities:
        sprite_list.add(tower_entity.sprite)
        if tower_entity.light_sprite:
          sprite_list.add(tower_entity.light_sprite)

    # render all the sprites
    sprite_list.draw(screen)
