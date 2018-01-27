import pygame
import Beam

def RenderBeams(screen, beams):

    beam_framebuffer = pygame.surface.Surface((640, 480), pygame.SRCALPHA, 32)
    beam_framebuffer = beam_framebuffer.convert_alpha()
        
    for beam in beams:
        beam_origin = (beam.x_origin, beam.y_origin)
        beam_dest = (beam.x_dest, beam.y_dest)
        print(beam.beamType.width)
        pygame.draw.line(beam_framebuffer, beam.beamType.color, beam_origin, beam_dest, beam.beamType.width)

    screen.blit(beam_framebuffer, (0, 0))

    # Todo:  Do more stuff here
