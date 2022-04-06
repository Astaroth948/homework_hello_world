from homework_2.src.Figure import Figure
from math import sqrt


class Triangle(Figure):

    name = "Triangle"

    def __init__(self, a, b, c):
        for side in [a, b, c]:
            if type(side) not in [int, float]:
                raise ValueError(
                    "Стороны должны быть указаны числовыми значениями"
                )

        if max(a, b, c) < (a + b + c) - max(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError(
                f"Треугольника со сторонами {a}, {b} и {c} не существует"
            )

    @property
    def area(self):
        p = self.perimeter / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
