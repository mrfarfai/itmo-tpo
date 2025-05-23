import unittest
import math
import random

def arccos_series(x, eps=1e-10):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a numeric type")
    if math.isnan(x) or math.isinf(x):
        raise ValueError("x must be a finite number")
    if x < -1 or x > 1:
        raise ValueError("x must be in [-1, 1]")

    if x == 1:
        return 0.0
    if x == -1:
        return math.pi

    sum_series = 0.0
    n = 0
    while True:
        coeff = math.factorial(2*n) / ((4**n) * (math.factorial(n)**2) * (2*n + 1))
        term = coeff * (x**(2*n + 1))
        if abs(term) < eps:
            break
        sum_series += term
        n += 1

    return math.pi/2 - sum_series

class TestArccosSeries(unittest.TestCase):
    TOL = 1e-8

    def test_arccos_0(self):
        """
        Тест для x = 0:
        Проверяется, что арккосинус для x = 0 возвращает значение pi/2.
        """
        x = 0.0
        result = arccos_series(x, eps=1e-12)
        expected = math.acos(x)
        self.assertAlmostEqual(result, expected, delta=self.TOL,
            msg=f"arccos_series({x}) = {result}, expected {expected}")

    def test_arccos_positive_half(self):
        """
        Тест для x = 0.5:
        Проверяется, что арккосинус для x = 0.5 возвращает ожидаемое значение.
        """
        x = 0.5
        result = arccos_series(x, eps=1e-12)
        expected = math.acos(x)
        self.assertAlmostEqual(result, expected, delta=self.TOL,
            msg=f"arccos_series({x}) = {result}, expected {expected}")

    def test_arccos_negative_half(self):
        """
        Тест для x = -0.5:
        Проверяется, что арккосинус для x = -0.5 возвращает ожидаемое значение.
        """
        x = -0.5
        result = arccos_series(x, eps=1e-12)
        expected = math.acos(x)
        self.assertAlmostEqual(result, expected, delta=self.TOL,
            msg=f"arccos_series({x}) = {result}, expected {expected}")

    def test_arccos_near_one(self):
        """
        Тесты для значений, близких к 1 и -1:
        Проверяется, что арккосинус для значений, близких к 1 и -1 (0.9 и -0.9), работает корректно.
        """
        for x in (0.9, -0.9):
            with self.subTest(x=x):
                result = arccos_series(x, eps=1e-12)
                expected = math.acos(x)
                self.assertAlmostEqual(result, expected, delta=self.TOL,
                    msg=f"arccos_series({x}) = {result}, expected {expected}")

    def test_arccos_endpoints(self):
        """
        Тест для крайних значений x = 1 и x = -1:
        Проверяется, что арккосинус для x = 1 равен 0, а для x = -1 равен pi.
        """
        self.assertEqual(arccos_series(1.0, eps=1e-12), 0.0)
        self.assertEqual(arccos_series(-1.0, eps=1e-12), math.pi)

    def test_arccos_out_of_domain(self):
        """
        Тест для значений за пределами области определения [-1, 1]:
        Проверяется, что значения, выходящие за пределы области определения, вызывают исключение ValueError.
        """
        for x in (1.0001, -1.0001):
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    arccos_series(x, eps=1e-8)

    def test_arccos_nan_inf(self):
        """
        Тест для NaN и бесконечности:
        Проверяется, что NaN, +∞ и -∞ вызывают исключение ValueError.
        """
        for x in (math.nan, math.inf, -math.inf):
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    arccos_series(x, eps=1e-8)

    def test_arccos_invalid_type(self):
        """
        Тест для недопустимых типов данных:
        Проверяется, что для строк и None вызывается исключение TypeError.
        """
        with self.assertRaises(TypeError):
            arccos_series("not a number", eps=1e-8)
        with self.assertRaises(TypeError):
            arccos_series(None, eps=1e-8)

    def test_arccos_random_in_domain(self):
        """
        Тест для случайных значений в допустимом диапазоне [-1, 1]:
        Генерируются случайные значения в диапазоне [-1, 1], и для них проверяется точность вычисления.
        """
        for _ in range(20):
            x = random.uniform(-1, 1)
            result = arccos_series(x, eps=1e-12)
            expected = math.acos(x)
            error = abs(result - expected)
            self.assertLess(error, self.TOL,
                msg=f"arccos_series({x:.6f}) error {error:.6e}")

    def test_arccos_small_values(self):
        """
        Тест для очень маленьких значений x (например, 1e-6 и -1e-6):
        Проверяется, что функция корректно работает с очень малыми значениями.
        """
        for x in [1e-6, -1e-6]:
            result = arccos_series(x, eps=1e-12)
            expected = math.acos(x)
            self.assertAlmostEqual(result, expected, delta=self.TOL,
                                   msg=f"arccos_series({x}) = {result}, expected {expected}")

    def test_arccos_large_values(self):
        """
        Тест для значений, выходящих за пределы диапазона [-1, 1]:
        Проверяется, что для значений, превышающих пределы области определения, функция вызывает исключение ValueError.
        """
        for x in [100, -100]:
            with self.assertRaises(ValueError):
                arccos_series(x, eps=1e-8)

    def test_arccos_precision(self):
        """
        Тест на большую точность с eps = 1e-15:
        Проверяется, что для высокой точности (eps = 1e-15) функция корректно вычисляет значение.
        """
        x = 0.5
        result = arccos_series(x, eps=1e-15)
        expected = math.acos(x)
        self.assertAlmostEqual(result, expected, delta=self.TOL,
                               msg=f"arccos_series({x}) = {result}, expected {expected}")

if __name__ == "__main__":
    unittest.main()
