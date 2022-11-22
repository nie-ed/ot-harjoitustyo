import pygame
from .shapes import Shapes
import random


class NewPiece(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
     
        self.shape = random.choice(Shapes.shapes_list)
        self.color = Shapes.shape_colors[Shapes.shapes_list.index(self.shape)]

        self.rotation = 0
