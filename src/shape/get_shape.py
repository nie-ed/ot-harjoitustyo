import random
from shape.shapes import Shapes

class GetShape():
    def __init__(self):
        self.shape = random.choice(Shapes.shapes_list)
        self.color = Shapes.shape_colors[Shapes.shapes_list.index(self.shape)]
        self.rotation = 0


    def change_rotation(self, rotation):
        self.rotation = rotation

