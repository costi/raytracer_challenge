class Tuple:
    """
    Class for holding points and vecotrs. Points have w=1.0 and Vectors have w=0.0
    """

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return self.w == 1.0

    def is_vector(self):
        return self.w == 0.0

    def __str__(self):
        return f"Tuple({self.x}, {self.y}, {self.z}, {self.w}). {self.is_point() = }"
