import pytest
from homework_2.src.Triangle import Triangle

NAME_FIGURE = "Triangle"
POSITIVE_DATA_1 = (5, 7.5, 6)
POSITIVE_DATA_2 = (3, 4, 2)
AREA_1 = 14.952920910310468
PERIMETER_1 = 18.5
SUM_AREA = 17.85765841996603
ERROR_INCORRECT_CLASS = "В функцию сложения площадей передан некорректный класс"
ERROR_INCORRECT_SIDES = "Треугольника со сторонами &-a, &-b и &-c не существует"
ERROR_NON_DIGIT = "Стороны должны быть указаны числовыми значениями"
NEGATIVE_DATA_1 = (5, 7.5, 0)
NEGATIVE_DATA_2 = (5, 7.5, "6")


def test_name_triangle():
    a, b, c = POSITIVE_DATA_1

    triangle = Triangle(a, b, c)
    assert triangle.name == NAME_FIGURE, f"Имя фигуры не {NAME_FIGURE}"


def test_area_triangle():
    a, b, c = POSITIVE_DATA_1

    triangle = Triangle(a, b, c)
    assert triangle.area == AREA_1, "Площадь рассчитана неправильно"


def test_perimeter_triangle():
    a, b, c = POSITIVE_DATA_1

    triangle = Triangle(a, b, c)
    assert triangle.perimeter == PERIMETER_1, "Периметр рассчитан неправильно"


def test_sum_area_triangles():
    a_1, b_1, c_1 = POSITIVE_DATA_1
    a_2, b_2, c_2 = POSITIVE_DATA_2

    triangle_1 = Triangle(a_1, b_1, c_1)
    triangle_2 = Triangle(a_2, b_2, c_2)

    assert triangle_1.add_area(
        triangle_2,
    ) == SUM_AREA, "Сумма площадей треугольников рассчитана неправильно"


def test_sum_area_triangles_with_incorrect_class():
    a, b, c = POSITIVE_DATA_1

    triangle = Triangle(a, b, c)

    with pytest.raises(ValueError) as context:
        triangle.add_area(b)
    assert ERROR_INCORRECT_CLASS == str(
        context.value,
    ), "Не сработала проверка на класс в методе add_area"


def test_create_impossible_triangle():
    a, b, c = NEGATIVE_DATA_1
    with pytest.raises(ValueError) as context:
        Triangle(a, b, c)
    assert ERROR_INCORRECT_SIDES.replace(
        "&-a", str(a)).replace("&-b", str(b)).replace("&-c", str(c)) == str(context.value), "Не сработала проверка на невозможные параметры сторон треугольника"


def test_create_triangle_with_non_digit_side():
    a, b, c = NEGATIVE_DATA_2
    with pytest.raises(ValueError) as context:
        Triangle(a, b, c)
    assert ERROR_NON_DIGIT == str(
        context.value,
    ), "Не сработала проверка нецифровые значения сторон"
