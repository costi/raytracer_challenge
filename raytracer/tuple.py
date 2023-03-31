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

    def __add__(self, other):
        """ Overrides + operator """
        if isinstance(other, Tuple):
            return Tuple(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z,
                self.w + other.w
                )
    def __sub__(self, other):
        """ Overrides - operator """
        if isinstance(other, Tuple):
            return Tuple(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
                self.w - other.w
            )

    def __mul__(self, multiplier):
        """ Overrides * operator """
        if isinstance(multiplier, float):
            return Tuple(
                self.x * multiplier,
                self.y * multiplier,
                self.z * multiplier,
                self.w * multiplier
            )

    def __neg__(self):
        """Overrides - (negation)"""
        return Tuple(-self.x, -self.y, -self.z, -self.w)


class Point(Tuple):
    """
    Point is a tuple with w = 1
    Why w = 1?
    So that two points substracted is a vector = the distance between the points
    """

    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

class Vector(Tuple):
    """
    Vector is a tuple with w = 0
    Why w = 0?
    So that:
        Adding two vectors is a vector
        Adding a point to a vector is a point moved by that vector
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

    def __str__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'
