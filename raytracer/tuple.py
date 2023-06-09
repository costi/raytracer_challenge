import math
class Tuple:
    """
    Class for holding points and vectors. Points have w=1.0 and Vectors have w=0.0
    """
    EPSILON = 1e-5

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
        return f"Tuple({self.x:6.2f}, {self.y:6.2f}, {self.z:6.2f}, {self.w:1.0f}). {self.is_point() = }"

    def __eq__(self, other):
        """equal if if coordinates are same"""
        if isinstance(other, Tuple):
            return \
                math.isclose(self.x, other.x, rel_tol = Tuple.EPSILON) and \
                math.isclose(self.y, other.y, rel_tol = Tuple.EPSILON) and \
                math.isclose(self.z, other.z, rel_tol = Tuple.EPSILON) and \
                math.isclose(self.w, other.w, rel_tol = Tuple.EPSILON)

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

    def __truediv__(self, divisor):
        """ Overrides / operator """
        if isinstance(divisor, float):
            return Tuple(
                self.x / divisor,
                self.y / divisor,
                self.z / divisor,
                self.w / divisor
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

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    def dot(self, other) -> float:
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def cross(a, b):
        return Vector(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x
        )
