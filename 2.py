import unittest

from binomial_queue import BinomialQueue


class TestBinomialQueue(unittest.TestCase):
    TOL = 1e-8

    def test_insert(self):
        """
        Тест для вставки элементов в очередь:
        Проверяется, что минимальный элемент правильный после нескольких вставок.
        """
        queue = BinomialQueue()
        queue.insert(5)
        queue.insert(3)
        queue.insert(8)
        queue.insert(1)

        self.assertEqual(queue.delete_min(), 1)

    def test_delete_min(self):
        """
        Тест для удаления минимального элемента:
        Проверяется корректность удаления минимального элемента.
        """
        queue = BinomialQueue()
        queue.insert(5)
        queue.insert(3)
        queue.insert(8)
        queue.insert(1)

        self.assertEqual(queue.delete_min(), 1)
        self.assertEqual(queue.delete_min(), 3)

        self.assertEqual(queue.delete_min(), 5)
        self.assertEqual(queue.delete_min(), 8)

    def test_merge(self):
        """
        Тест для слияния двух биномиальных куч:
        Проверяется корректность слияния двух куч.
        """
        queue1 = BinomialQueue()
        queue2 = BinomialQueue()

        queue1.insert(5)
        queue1.insert(10)
        queue2.insert(3)
        queue2.insert(7)

        queue1.merge(queue2)

        self.assertEqual(queue1.delete_min(), 3)
        self.assertEqual(queue1.delete_min(), 5)
        self.assertEqual(queue1.delete_min(), 7)
        self.assertEqual(queue1.delete_min(), 10)

    def test_empty_queue(self):
        """
        Тест для пустой очереди:
        Проверяется, что удаление из пустой очереди вызывает ошибку.
        """
        queue = BinomialQueue()
        with self.assertRaises(ValueError):
            queue.delete_min()

    def test_large_number_of_elements(self):
        """
        Тест для большого количества элементов:
        Проверяется, что функция корректно работает с большим количеством элементов.
        """
        queue = BinomialQueue()
        for i in range(1000, 0, -1):
            queue.insert(i)

        for i in range(1, 1001):
            self.assertEqual(queue.delete_min(), i)


if __name__ == "__main__":
    unittest.main()
