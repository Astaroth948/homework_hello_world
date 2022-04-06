import pytest
from homework_2.src.Circle import Circle

NAME_FIGURE = "Circle"
POSITIVE_DATA_1 = 7.5
POSITIVE_DATA_2 = 3
AREA_1 = 176.71458676442586
PERIMETER_1 = 47.12388980384689
SUM_AREA = 204.988920646734
ERROR_INCORRECT_CLASS = "В функцию сложения площадей передан некорректный класс"
ERROR_INCORRECT_SIDES = "Окружности с радиусом &-r не существует"
ERROR_NON_DIGIT = "Радиус должен быть указан числовым значением"
NEGATIVE_DATA_1 = 0
NEGATIVE_DATA_2 = "6"


def test_name_circle():
    r = POSITIVE_DATA_1

    circle = Circle(r)
    assert circle.name == NAME_FIGURE, f"Имя фигуры не {NAME_FIGURE}"


def test_area_circle():
    r = POSITIVE_DATA_1

    circle = Circle(r)
    assert circle.area == AREA_1, "Площадь рассчитана неправильно"


def test_perimeter_circle():
    r = POSITIVE_DATA_1

    circle = Circle(r)
    assert circle.perimeter == PERIMETER_1, "Периметр рассчитан неправильно"


def test_sum_area_circles():
    r_1 = POSITIVE_DATA_1
    r_2 = POSITIVE_DATA_2

    circle_1 = Circle(r_1)
    circle_2 = Circle(r_2)

    assert circle_1.add_area(
        circle_2,
    ) == SUM_AREA, "Сумма площадей окружностей рассчитана неправильно"


def test_sum_area_circles_with_incorrect_class():
    r = POSITIVE_DATA_1

    circle = Circle(r)

    with pytest.raises(ValueError) as context:
        circle.add_area(r)
    assert ERROR_INCORRECT_CLASS == str(
        context.value,
    ), "Не сработала проверка на класс в методе add_area"


def test_create_impossible_circle():
    r = NEGATIVE_DATA_1
    with pytest.raises(ValueError) as context:
        Circle(r)
    assert ERROR_INCORRECT_SIDES.replace(
        "&-r", str(r)) == str(context.value), "Не сработала проверка на невозможные параметры радиуса окружности"


def test_create_circle_with_non_digit_radius():
    r = NEGATIVE_DATA_2
    with pytest.raises(ValueError) as context:
        Circle(r)
    assert ERROR_NON_DIGIT == str(
        context.value,
    ), "Не сработала проверка нецифровое значение радиуса"
