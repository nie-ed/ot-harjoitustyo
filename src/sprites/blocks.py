import pygame


class Blocks(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0, color=None):# pylint: disable=invalid-name
        super().__init__()

        self.image = pygame.Surface((29, 29))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
