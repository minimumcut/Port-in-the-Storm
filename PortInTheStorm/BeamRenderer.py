import math
import pygame
import Beam
from Constants import PIXEL_RESOLUTION, RESOLUTION_X, RESOLUTION_Y

def RenderBeams(screen, beams):

    beam_framebuffer = pygame.surface.Surface((RESOLUTION_X, RESOLUTION_Y), pygame.SRCALPHA, 32)
    beam_framebuffer = beam_framebuffer.convert_alpha()
    half_pix_res = PIXEL_RESOLUTION/2
    # half_pix_res = 0

    for beam in beams:

        beam_origin =  (half_pix_res + PIXEL_RESOLUTION * beam.x_origin, half_pix_res + PIXEL_RESOLUTION * beam.y_origin)
        beam_dest =  (half_pix_res + PIXEL_RESOLUTION * beam.x_dest, half_pix_res + PIXEL_RESOLUTION * beam.y_dest)
        pygame.draw.line(beam_framebuffer, beam.beamType.color, beam_origin, beam_dest, beam.beamType.width)

    screen.blit(beam_framebuffer, (0, 0))
    # beam_img = pygame.image.load('sprites/LBstraight.png')
    # half_pix_res = PIXEL_RESOLUTION/2
    # half_pix_res = 0

    # original_size_x, original_size_y = beam_img.get_size()

    # for beam in beams:
    #     # import pdb; pdb.set_trace()
    #     beam_origin =  (half_pix_res + PIXEL_RESOLUTION * beam.x_origin, half_pix_res + PIXEL_RESOLUTION * beam.y_origin)
    #     beam_dest =  (half_pix_res + PIXEL_RESOLUTION * beam.x_dest, half_pix_res + PIXEL_RESOLUTION * beam.y_dest)
    #     # stretch image
    #     dx = abs(beam.x_dest - beam.x_origin)
    #     dy = abs(beam.y_dest - beam.y_origin)
    #     length = int(math.sqrt(dx * dx + dy * dy)) * 64
    #     # import pdb; pdb.set_trace()

    #     stretched_img = beam_img.copy()
    #     stretched_img = pygame.transform.scale(beam_img, (int(original_size_x), length))
    #     # import pdb; pdb.set_trace()
    #     # stretched
    #     # stretched_img = beam_img
    #     if beam_origin[0] > beam_dest[0] and beam_origin[1] > beam_dest[1]:
    #         rot_angle = 45
    #         print("NW")
    #         # facing NW from origin
    #     elif beam_origin[0] > beam_dest[0] and beam_origin[1] == beam_dest[1]:
    #         rot_angle = 90
    #         print("W")
    #         # facing W from origin
    #     elif beam_origin[0] > beam_dest[0] and beam_origin[1] < beam_dest[1]:
    #         rot_angle = 135
    #         print("SW")
    #         # facing SW from origin
    #     elif beam_origin[0] == beam_dest[0] and beam_origin[1] < beam_dest[1]:
    #         rot_angle = 180
    #         print("S")
    #         # facing S from origin
    #     elif beam_origin[0] < beam_dest[0] and beam_origin[1] < beam_dest[1]:
    #         rot_angle = 225
    #         print("SE")
    #         # facing SE from origin
    #     elif beam_origin[0] < beam_dest[0] and beam_origin[1] == beam_dest[1]:
    #         rot_angle = 270
    #         print("E")
    #         # facing E from origin. default position
    #     elif beam_origin[0] < beam_dest[0] and beam_origin[1] > beam_dest[1]:
    #         rot_angle = 315
    #         print("NE")
    #         # facing NE from origin
    #     else:
    #         rot_angle = 0
    #         print("N")
    #         # rot angle is 0

    #     # orig_rect = stretched_img.get_rect()
    #     # rot_image = pygame.transform.rotate(stretched_img, rot_angle)
    #     # rot_rect = orig_rect.copy()
    #     # rot_rect.center = rot_image.get_rect().center
    #     # rot_image = rot_image.subsurface(rot_rect).copy()

    #     # import pdb; pdb.set_trace()
    #     # loc = stretched_img.get_rect().center
    #     rot_image = pygame.transform.rotate(stretched_img, rot_angle)
    #     # rot_image.get_rect().center = loc
    #     print("beam origin", beam_origin)
    #     print("length", length)
    #     print("rot image center", rot_image.get_rect().center)
    #     # screen.blit(rot_image, (int((beam.x_dest + beam.x_origin)*64/2), int((beam.y_dest + beam.y_origin)*64/2)))
    #     # screen.blit(rot_image, (beam_origin[0] + PIXEL_RESOLUTION * (beam.x_dest - beam.x_origin), beam_origin[1] + PIXEL_RESOLUTION * (beam.y_dest - beam.y_origin) ) )
    #     screen.blit(rot_image, (beam_origin[0], beam_origin[1]))
    # for beam in beams:

    #     beam_origin =  (half_pix_res + PIXEL_RESOLUTION * beam.x_origin, half_pix_res + PIXEL_RESOLUTION * beam.y_origin)
    #     beam_dest =  (half_pix_res + PIXEL_RESOLUTION * beam.x_dest, half_pix_res + PIXEL_RESOLUTION * beam.y_dest)
    #     pygame.draw.line(beam_framebuffer, beam.beamType.color, beam_origin, beam_dest, beam.beamType.width)

    # screen.blit(beam_framebuffer, (0, 0))
