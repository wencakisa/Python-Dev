from .simple import Circle


class RegularPolygon(Circle):
    def __init__(self, radius, sides, **kwargs):
        super().__init__(radius=radius, **kwargs)
        self.sides = sides

    def draw_circle(self, turtle):
        turtle.circle(self.radius, steps=self.sides)


class Triangle(RegularPolygon):
    def __init__(self, area, **kwargs):
        super().__init__(radius=area, sides=3, **kwargs)


class Pie(RegularPolygon):
    pass
