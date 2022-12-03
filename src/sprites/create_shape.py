import random
import pygame
from .shapes import Shapes

class CreateShapes(pygame.sprite.Sprite):
    def __init__(self,  X=0, Y=0):
        super().__init__()
        self.shape = random.choice(Shapes.shapes_list)
        self.rotation = 0
        self.color = Shapes.shape_colors[Shapes.shapes_list.index(self.shape)]

        self.indexes = []
        objects = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(objects):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.indexes.append((X + j, Y + i))

        for i, index in enumerate(self.indexes):
            self.indexes[i] = (index[0] - 2, index [1] -4)



