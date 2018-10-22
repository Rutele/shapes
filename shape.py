# coding: utf8


class Shape(object):
    """
    Base class for all shapes.
    """
    x = None
    y = None

    def __init__(self, pos):
        self.pos = pos

    def area(self):
        """
        Abstract method returning area of a shape.
        """

    def perimeter(self):
        """
        Abstract method returning shape perimeter.
        """

    def summary(self):
        """
        Return summary of a shape.
        """
        return {
            'area': self.area(),
            'perimeter': self.perimeter()
        }

    def draw(self, screen):
        """
        Draws the given shape
        """