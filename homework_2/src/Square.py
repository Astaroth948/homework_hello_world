from homework_2.src.Figure import Figure


class Square(Figure):

    name = "Square"

    def __init__(self, a):
        if type(a) not in [int, float]:
            raise ValueError(
                "Стороны должны быть указаны числовыми значениями"
            )

        if a > 0:
            self.a = a
        else:
            raise ValueError(
                f"Квадрата со сторонами {a} не существует"
            )

    @property
    def area(self):
        return self.a**2

    @property
    def perimeter(self):
        return self.a * 4
