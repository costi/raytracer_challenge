class Tuple:
    """
    Class for holding points and vectors. Points have w=1.0 and Vectors have w=0.0
    """

    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def is_point(self):
        return self.w == 1.0

    def is_vector(self):
        return self.w == 0.0

    def __str__(self):
        return f"Tuple({self.x}, {self.y}, {self.z}, {self.w}). {self.is_point() = }"

    def __eq__(self, other):
        """equal if if coordinates are same"""
        if isinstance(other, Tuple):
            return self.x == other.x and \
                self.y == other.y and \
                    self.z == other.z and \
                        self.w == other.w

class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.z})'
