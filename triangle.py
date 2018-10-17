from shape import Shape
import numpy as np


class Triangle(Shape):
    """
    Triangular shape

    a and b are two dimensional vectors
    """

    a = None
    b = None
    c = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

        if np.abs(self.a) == 0 or np.abs(self.b) == 0:
            raise ValueError("Vectors cannot have zero length.")

        self.c = a - b

    def area(self):
        return 0.5 * np.abs(self.a[0] * self.b[1] - self.a[1] * self.b[0])

    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(self.c)

    def __str__(self):
        return "Triangle with sides a:{}, b:{}, c:{})".format(self.a, self.b, self.c)

    def __repr__(self):
        return "Triangle({},{})".format(self.a, self.b)
