import pygame


class Blocks(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, color=None):
        super().__init__()

        self.image = pygame.Surface((29,29))
        self.image.fill(color)

        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
