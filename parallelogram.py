from shape import Shape
import numpy as np
import pygame


class Parallelogram(Shape):

    a = None
    b = None
    alpha = None
    __deg = None

    def __init__(self, pos, a, b, alpha):
        super().__init__(pos)
        self.a = a
        self.b = b

        if alpha >= 90 or alpha <= 0:
            raise ValueError("The angle has to be between 0° and 90° degrees")

        self.__deg = alpha
        self.alpha = np.pi * alpha / 180

    def area(self):
        return self.a * self.b * np.sin(self.alpha)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Parallelogram with dimensions of {} x {} and angle {} between sides.".format(self.a, self.b, self.__deg)

    def __repr__(self):
        return "Parallelogram({}, {}, {})".format(self.a, self.b, self.__deg)

    def draw(self, screen):
        h = np.ceil(self.b * np.sin(self.alpha)) * 50
        dx = np.ceil(self.b * np.cos(self.alpha)) * 50
        points = [self.pos, (self.pos[0] + self.a * 50, self.pos[1]), (self.pos[0] + self.a * 50 + dx, self.pos[1] - h), \
                  (self.pos[0] + dx, self.pos[1] - h)]
        return pygame.draw.polygon(screen, (255, 255, 255), points)


class Rhombus(Parallelogram):

    def __init__(self, a, alpha):
        super().__init__(a, a, alpha)
