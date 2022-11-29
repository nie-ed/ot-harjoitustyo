import pygame

class CreateShapes(pygame.sprite.Sprite):
    def __init__(self,  shape):
        super().__init__()

        self.indexes = []
        objects = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(objects):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.indexes.append((shape.x + j, shape.y + i))

        for i, index in enumerate(self.indexes):
            self.indexes[i] = (index[0] - 2, index [1] -4)
