import pytest
from homework_2.src.Square import Square

NAME_FIGURE = "Square"
POSITIVE_DATA_1 = 7.5
POSITIVE_DATA_2 = 3
AREA_1 = 56.25
PERIMETER_1 = 30.0
SUM_AREA = 65.25
ERROR_INCORRECT_CLASS = "В функцию сложения площадей передан некорректный класс"
ERROR_INCORRECT_SIDES = "Квадрата со сторонами &-a не существует"
ERROR_NON_DIGIT = "Стороны должны быть указаны числовыми значениями"
NEGATIVE_DATA_1 = 0
NEGATIVE_DATA_2 = "6"


def test_name_square():
    a = POSITIVE_DATA_1

    square = Square(a)
    assert square.name == NAME_FIGURE, f"Имя фигуры не {NAME_FIGURE}"


def test_area_square():
    a = POSITIVE_DATA_1

    square = Square(a)
    assert square.area == AREA_1, "Площадь рассчитана неправильно"


def test_perimeter_square():
    a = POSITIVE_DATA_1

    square = Square(a)
    assert square.perimeter == PERIMETER_1, "Периметр рассчитан неправильно"


def test_sum_area_squares():
    a_1 = POSITIVE_DATA_1
    a_2 = POSITIVE_DATA_2

    square_1 = Square(a_1)
    square_2 = Square(a_2)

    assert square_1.add_area(
        square_2,
    ) == SUM_AREA, "Сумма площадей квадратов рассчитана неправильно"


def test_sum_area_squares_with_incorrect_class():
    a = POSITIVE_DATA_1

    square = Square(a)

    with pytest.raises(ValueError) as context:
        square.add_area(a)
    assert ERROR_INCORRECT_CLASS == str(
        context.value,
    ), "Не сработала проверка на класс в методе add_area"


def test_create_impossible_square():
    a = NEGATIVE_DATA_1
    with pytest.raises(ValueError) as context:
        Square(a)
    assert ERROR_INCORRECT_SIDES.replace(
        "&-a", str(a)) == str(context.value), "Не сработала проверка на невозможные параметры сторон квадрата"


def test_create_square_with_non_digit_side():
    a = NEGATIVE_DATA_2
    with pytest.raises(ValueError) as context:
        Square(a)
    assert ERROR_NON_DIGIT == str(
        context.value,
    ), "Не сработала проверка нецифровые значения сторон"
