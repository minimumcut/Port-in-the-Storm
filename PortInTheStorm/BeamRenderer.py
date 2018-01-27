import pygame
import Beam

def RenderBeams(screen, beams):

    beam_framebuffer = pygame.surface.Surface((1280, 704), pygame.SRCALPHA, 32)
    beam_framebuffer = beam_framebuffer.convert_alpha()
        
    for beam in beams:
        beam_origin =  (16 + 32 * beam.x_origin, 16 + 32 * beam.y_origin)
        beam_dest =  (16 + 32 * beam.x_dest, 16 + 32 * beam.y_dest)
        pygame.draw.line(beam_framebuffer, beam.beamType.color, beam_origin, beam_dest, beam.beamType.width)

    screen.blit(beam_framebuffer, (0, 0))

    # Todo:  Do more stuff here
