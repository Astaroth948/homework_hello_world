from homework_2.src.Figure import Figure
from math import pi


class Circle(Figure):

    name = "Circle"

    def __init__(self, r):
        if type(r) not in [int, float]:
            raise ValueError(
                "Радиус должен быть указан числовым значением"
            )

        if r > 0:
            self.r = r
        else:
            raise ValueError(
                f"Окружности с радиусом {r} не существует"
            )

    @property
    def area(self):
        return pi * self.r**2

    @property
    def perimeter(self):
        return 2 * pi * self.r
