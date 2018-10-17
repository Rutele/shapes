# coding: utf8
import rectangles
import circle
import triangle

import numpy as np


vec1 = np.array([0, 4])
vec2 = np.array([4, 0])

tri1 = triangle.Triangle(vec1, vec2)
print(tri1.summary())