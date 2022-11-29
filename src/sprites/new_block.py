import random
import pygame
from .shapes import Shapes


class NewBlockAttributes(pygame.sprite.Sprite):
    def __init__(self, X, Y):# pylint: disable=invalid-name
        super().__init__()

        self.shape = random.choice(Shapes.shapes_list)
        self.rotation = 0
        self.rect = None
        self.x = X# pylint: disable=invalid-name
        self.y = Y# pylint: disable=invalid-name
        self.color = Shapes.shape_colors[Shapes.shapes_list.index(self.shape)]
