import pygame

light=pygame.image.load("fx/vignette_mask.png")
filter = pygame.surface.Surface((640, 480))
filter.fill(pygame.color.Color('Grey'))
filter.blit(light, (0, 0))

def RenderVignette(screen):
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)