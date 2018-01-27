import copy
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos=0, angle=0, frames=None):
        # current frames will be the ones being animated
        # original frames will be stored to prevent data loss when rotating
        super(Sprite, self).__init__()
        self.frames = frames
        self.current_frames = copy.deepcopy(self.frames)
        self.animation = self.stand_animation()
        self.image = frames[0][0]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.angle = angle

    def stand_animation(self):
        while True:
            for current_frame in self.current_frames[0]:
                self.image = current_frame
                yield None
                yield None

    def update(self, *args):
        self.animation.next()

    def rotate_frames(self, angle):
        self.angle = (self.angle + angle) % 360
        print(self.angle)
        new_frames = []
        for frame in self.frames[0]:
            new_frames.append(self.rotate_along_center(frame, self.angle))

        self.current_frames[0] = new_frames
        self.image = self.current_frames[0][0]

    @staticmethod
    def rotate_along_center(image, angle):
        # rotate an image while keeping its center and size
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

