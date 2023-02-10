import unittest

from katas.kyu_4.counting_change_combinations import (
    count_change, count_change_second_solution)


class CountChangeTestCase(unittest.TestCase):
    def test_count_change(self):
        self.assertEqual(count_change(4, [1, 2]), 3)
        self.assertEqual(count_change(10, [5, 2, 3]), 4)
        self.assertEqual(count_change(11, [5, 7]), 0)

    def test_count_change_second_solution(self):
        self.assertEqual(count_change_second_solution(4, [1, 2]), 3)
        self.assertEqual(count_change_second_solution(10, [5, 2, 3]), 4)
        self.assertEqual(count_change_second_solution(11, [5, 7]), 0)
