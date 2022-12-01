import unittest
from katas.kyu_6.find_the_unique_number import find_uniq, find_uniq_second_solution


class FindUniqTestCase(unittest.TestCase):
    def test_find_uniq(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 3, 10, 3, 3, 3]), 10)
        self.assertEqual(find_uniq([14, 1, 1, 1, 1, 1, 1]), 14)

    def test_find_uniq_second_solution(self):
        self.assertEqual(find_uniq_second_solution([1, 1, 1, 1, 2, 1]), 2)
        self.assertEqual(find_uniq_second_solution([3, 1, 1, 1, 1, 1]), 3)
        self.assertEqual(find_uniq_second_solution([1, 1, 111, 1, 1, 1]), 111)
