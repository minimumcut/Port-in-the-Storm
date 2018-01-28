import pygame

import Sprite

from Constants import RESOLUTION_X, RESOLUTION_Y

# Bad practice - oh well
light=pygame.image.load("fx/vignette_mask.png")
filter = pygame.surface.Surface((RESOLUTION_X, RESOLUTION_Y))
filter.fill(pygame.color.Color('Grey'))
filter.blit(light, (0, 0))

lights=["fx/rain1.png", "fx/rain2.png", "fx/rain3.png", "fx/rain4.png", "fx/rain5.png", "fx/rain6.png"]
light_imgs = [list(map(lambda img_path: pygame.image.load(img_path), lights))]
light_sprite = Sprite.Sprite(0,0, light_imgs)

def RenderVignette(screen):
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

def RenderRain(screen):
    screen.blit(light_sprite.image, (0, 0))
    light_sprite.update()

def RenderScreenMask(screen):
    s = pygame.Surface((RESOLUTION_X,RESOLUTION_Y), pygame.SRCALPHA)
    s.fill((0,0,0,128))
    screen.blit(s, (0,0))

def RenderOpaqueScreenMask(screen):
    s = pygame.Surface((RESOLUTION_X,RESOLUTION_Y), pygame.SRCALPHA)
    s.fill((0,0,0,255))
    screen.blit(s, (0,0))