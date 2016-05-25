from .base import Figure


class Circle(Figure):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw_figure(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)
        turtle.pendown()
        turtle.color(self.color)
        self.draw_circle(turtle)

    def draw_circle(self, turtle):
        turtle.circle(self.radius)


class Rectangle(Figure):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw_figure(self, turtle):
        half_width = self.width / 2
        half_height = self.height / 2
        left = self.center_x - half_width
        top = self.center_y - half_height

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)

        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)


class Square(Rectangle):
    def __init__(self, side, **kwargs):
        super().__init__(width=side, height=side, **kwargs)
