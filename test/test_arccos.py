import pytest
import math
import random
from src.arccos_model import arccos_series


def check_arccos(x, eps, expected):
    result = arccos_series(x, eps)
    assert abs(result - expected) < 1e-8, f"arccos_series({x}) = {result}, expected {expected}"


@pytest.mark.parametrize("x, expected", [(0.0, math.pi / 2), (0.5, math.acos(0.5)), (-0.5, math.acos(-0.5))])
def test_arccos_basic(x, expected):
    """ Проверяем базовые значения для x = 0, x = 0.5 и x = -0.5 """
    check_arccos(x, 1e-12, expected)


@pytest.mark.parametrize("x", [0.9, -0.9])
def test_arccos_near_one(x):
    """ Проверка значений близких к 1 и -1 """
    expected = math.acos(x)
    check_arccos(x, 1e-12, expected)


@pytest.mark.parametrize("x, expected", [(1.0, 0.0), (-1.0, math.pi)])
def test_arccos_endpoints(x, expected):
    """ Проверка для крайних значений x = 1 и x = -1 """
    check_arccos(x, 1e-12, expected)


@pytest.mark.parametrize("x", [1.0001, -1.0001])
def test_arccos_out_of_domain(x):
    """ Проверка значений за пределами области определения [-1, 1] """
    with pytest.raises(ValueError):
        arccos_series(x, eps=1e-8)


@pytest.mark.parametrize("x", [math.nan, math.inf, -math.inf])
def test_arccos_nan_inf(x):
    """ Проверка на NaN и бесконечность """
    with pytest.raises(ValueError):
        arccos_series(x, eps=1e-8)


@pytest.mark.parametrize("x", ["not a number", None])
def test_arccos_invalid_type(x):
    """ Проверка на недопустимые типы данных """
    with pytest.raises(TypeError):
        arccos_series(x, eps=1e-8)


@pytest.mark.parametrize("x", [random.uniform(-1, 1) for _ in range(20)])
def test_arccos_random_in_domain(x):
    """ Проверка случайных значений в допустимом диапазоне [-1, 1] """
    expected = math.acos(x)
    check_arccos(x, 1e-12, expected)


@pytest.mark.parametrize("x, expected", [(1e-6, math.acos(1e-6)), (-1e-6, math.acos(-1e-6))])
def test_arccos_small_values(x, expected):
    """ Проверка на очень маленькие значения x (например, 1e-6 и -1e-6) """
    check_arccos(x, 1e-12, expected)


@pytest.mark.parametrize("x", [100, -100])
def test_arccos_large_values(x):
    """ Проверка значений, выходящих за пределы диапазона [-1, 1] """
    with pytest.raises(ValueError):
        arccos_series(x, eps=1e-8)


@pytest.mark.parametrize("x, expected", [(0.5, math.acos(0.5))])
def test_arccos_precision(x, expected):
    """ Проверка точности с eps = 1e-15 """
    check_arccos(x, 1e-15, expected)


if __name__ == "__main__":
    pytest.main()
