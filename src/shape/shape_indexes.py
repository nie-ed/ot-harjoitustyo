class ShapeIndexes():
    def __init__(self, X=0, Y=0, shape=None, rotation=0):# pylint: disable=invalid-name
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
