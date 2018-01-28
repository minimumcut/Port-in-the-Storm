import pygame
import Beam
from Constants import PIXEL_RESOLUTION, RESOLUTION_X, RESOLUTION_Y

def RenderBeams(screen, beams):

    beam_framebuffer = pygame.surface.Surface((RESOLUTION_X, RESOLUTION_Y), pygame.SRCALPHA, PIXEL_RESOLUTION)
    beam_framebuffer = beam_framebuffer.convert_alpha()
    half_pix_res = PIXEL_RESOLUTION/2

    for beam in beams:

        beam_origin =  (half_pix_res + PIXEL_RESOLUTION * beam.x_origin, half_pix_res + PIXEL_RESOLUTION * beam.y_origin)
        beam_dest =  (half_pix_res + PIXEL_RESOLUTION * beam.x_dest, half_pix_res + PIXEL_RESOLUTION * beam.y_dest)
        pygame.draw.line(beam_framebuffer, beam.beamType.color, beam_origin, beam_dest, beam.beamType.width)

    screen.blit(beam_framebuffer, (0, 0))

    # Todo:  Do more stuff here
