import random
from shape.shapes import Shapes


class GetShape():
    """Class for choosing randompy next used piece.
    """

    def __init__(self):
        """Constructor for class. Gets piece shape, index and color.
        """
        self.shape = random.choice(Shapes.shapes_list)
        self.index = Shapes.shapes_list.index(self.shape)
        self.color = Shapes.shape_colors[self.index]
