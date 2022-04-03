from homework_2.src.Figure import Figure


class Rectangle(Figure):

    name = "Rectangle"

    def __init__(self, a, b):
        for side in [a, b]:
            if type(side) not in [int, float]:
                raise ValueError(
                    "Стороны должны быть указаны числовыми значениями"
                )

        if (a > 0) and (b > 0):
            self.a = a
            self.b = b
        else:
            raise ValueError(
                f"Прямогульника со сторонами {a} и {b} не существует"
            )

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2
