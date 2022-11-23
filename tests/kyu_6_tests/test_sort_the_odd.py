import unittest
from katas.kyu_6.sort_the_odd import sort_array, sort_array_second_solution


class SortArrayTestCase(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [1, 8, 3, 6, 5, 4, 7, 2, 9, 0])
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]), [])

    def test_sort_array_second_solution(self):
        self.assertEqual(sort_array_second_solution([8, 3, 2, 1, 66, 23]), [8, 1, 2, 3, 66, 23])
