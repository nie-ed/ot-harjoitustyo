class ShapeIndexes():
    """Class for getting the x and y coordinates of chosen piece.
    """
    def __init__(self, X=0, Y=0, shape=None, rotation=0):# pylint: disable=invalid-name
        """Constructor of class. Creates the list for x and y coordinates of piece.

        Args:
            X (int): x coordinate of block. Defaults to 0.
            Y (int): y coordinates of block. Defaults to 0.
            shape (Shape): Shape of piece, in a list. Defaults to None.
            rotation (int): Rotation of piece. Defaults to 0.
        """
        self.shape= shape
        self.rotation = rotation

        self.indexes = [] 
        self.objects = self.shape[self.rotation % len(self.shape)]
       

        for i, line in enumerate(self.objects):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.indexes.append((X + j, Y + i))

        for i, index in enumerate(self.indexes):
            self.indexes[i] = (index[0] - 2, index[1] -4)
