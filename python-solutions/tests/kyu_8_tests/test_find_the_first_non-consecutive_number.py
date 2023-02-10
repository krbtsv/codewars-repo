import unittest

from katas.kyu_8.find_the_first_non_consecutive_number import (
    first_non_consecutive, first_non_consecutive_second_solution)


class FirstNonConsecutiveTestCase(unittest.TestCase):
    def test_first_non_consecutive(self):
        self.assertEqual(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]), 6)
        self.assertEqual(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]), None)
        self.assertEqual(first_non_consecutive([4, 6, 7, 8, 9, 11]), 6)
        self.assertEqual(first_non_consecutive([4, 5, 6, 7, 8, 9, 11]), 11)
        self.assertEqual(first_non_consecutive([31, 32]), None)
        self.assertEqual(first_non_consecutive([-3, -2, 0, 1]), 0)
        self.assertEqual(first_non_consecutive([-5, -4, -3, -1]), -1)

    def test_first_non_consecutive_second_solution(self):
        self.assertEqual(first_non_consecutive_second_solution([1, 2, 3, 4, 6, 7, 8]), 6)
        self.assertEqual(first_non_consecutive_second_solution([1, 2, 3, 4, 5, 6, 7, 8]), None)
        self.assertEqual(first_non_consecutive_second_solution([4, 6, 7, 8, 9, 11]), 6)
        self.assertEqual(first_non_consecutive_second_solution([4, 5, 6, 7, 8, 9, 11]), 11)
        self.assertEqual(first_non_consecutive_second_solution([31, 32]), None)
        self.assertEqual(first_non_consecutive_second_solution([-3, -2, 0, 1]), 0)
        self.assertEqual(first_non_consecutive_second_solution([-5, -4, -3, -1]), -1)
