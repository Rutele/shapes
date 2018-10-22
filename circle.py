from shape import Shape
import numpy as np
import pygame


class Circle(Shape):
    """
    Circular shape
    """

    r = None

    def __init__(self, pos,r):
        super().__init__(pos)
        self.r = r

        if r <= 0:
            raise ValueError("Radius cannot be zero or negative.")

    def area(self):
        return self.r * np.pi ** 2

    def perimeter(self):
        return 2 * np.pi * self.r

    def __str__(self):
        return "Circle with radius {}".format(self.r)

    def __repr__(self):
        return "Circle({})".format(self.r)

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.pos, self.r * 50)