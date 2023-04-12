import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get("None", 0, "test"), "Отсутствует список")
        self.assertEqual(arrs.get([1, 2, 3], 5.4, "test"), "Индекс не целое число")
        self.assertEqual(arrs.get([1, 2, None], 2, "test"), "В списке элемент None")
        self.assertEqual(arrs.get([1, 2, 3], -1), None)


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1.1, 3), "Начальный индекс не целое число")
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 3.1), "Конечный индекс не целое число")
        self.assertEqual(arrs.my_slice("None", 1, 3), "Отсутствует список")
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, -3), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, -3), [])
        self.assertEqual(arrs.my_slice([1, 2], -3, -1), [1])
        self.assertEqual(arrs.my_slice([1, 2, "test", 3], 1, 3), [2, "test"])


