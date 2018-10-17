from shape import Shape


class Triangle(Shape):
    """
    Triangular shape
    """

    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        a.self = a
        b.self = b
        c.self = c
        