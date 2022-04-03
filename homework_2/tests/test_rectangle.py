import pytest
from homework_2.src.Rectangle import Rectangle

NAME_FIGURE = "Rectangle"
POSITIVE_DATA_1 = (5, 7.5)
POSITIVE_DATA_2 = (3, 4)
AREA_1 = 37.5
PERIMETER_1 = 25.0
SUM_AREA = 49.5
ERROR_INCORRECT_CLASS = "В функцию сложения площадей передан некорректный класс"
ERROR_INCORRECT_SIDES = "Прямогульника со сторонами &-a и &-b не существует"
ERROR_NON_DIGIT = "Стороны должны быть указаны числовыми значениями"
NEGATIVE_DATA_1 = (5, 0)
NEGATIVE_DATA_2 = (5, "6")


def test_name_rectangle():
    a, b = POSITIVE_DATA_1

    rectangle = Rectangle(a, b)
    assert rectangle.name == NAME_FIGURE, f"Имя фигуры не {NAME_FIGURE}"


def test_area_rectangle():
    a, b = POSITIVE_DATA_1

    rectangle = Rectangle(a, b)
    assert rectangle.area == AREA_1, "Площадь рассчитана неправильно"


def test_perimeter_rectangle():
    a, b = POSITIVE_DATA_1

    rectangle = Rectangle(a, b)
    assert rectangle.perimeter == PERIMETER_1, "Периметр рассчитан неправильно"


def test_sum_area_rectangles():
    a_1, b_1 = POSITIVE_DATA_1
    a_2, b_2 = POSITIVE_DATA_2

    rectangle_1 = Rectangle(a_1, b_1)
    rectangle_2 = Rectangle(a_2, b_2)

    assert rectangle_1.add_area(
        rectangle_2,
    ) == SUM_AREA, "Сумма площадей прямоугольников рассчитана неправильно"


def test_sum_area_rectangles_with_incorrect_class():
    a, b = POSITIVE_DATA_1

    rectangle = Rectangle(a, b)

    with pytest.raises(ValueError) as context:
        rectangle.add_area(b)
    assert ERROR_INCORRECT_CLASS == str(
        context.value,
    ), "Не сработала проверка на класс в методе add_area"


def test_create_impossible_rectangle():
    a, b = NEGATIVE_DATA_1
    with pytest.raises(ValueError) as context:
        Rectangle(a, b)
    assert ERROR_INCORRECT_SIDES.replace(
        "&-a", str(a)).replace("&-b", str(b)) == str(context.value), "Не сработала проверка на невозможные параметры сторон прямоугольника"


def test_create_rectangle_with_non_digit_side():
    a, b = NEGATIVE_DATA_2
    with pytest.raises(ValueError) as context:
        Rectangle(a, b)
    assert ERROR_NON_DIGIT == str(
        context.value,
    ), "Не сработала проверка нецифровые значения сторон"
