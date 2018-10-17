# coding: utf8
from shape import Shape


class Rectangle(Shape):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

        if self.a <= 0 or self.b <=0:
            raise ValueError("Size cannot be negative or zero")

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Rectangle of dimensions {} x {}".format(self.a, self.b)

    def __repr__(self):
        return "Rectangle({},{})".format(self.a, self.b)


class Square(Rectangle):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a)
