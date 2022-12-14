import unittest
from katas.kyu_6.two_sum import two_sum, two_sum_second_solution


class TwoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([1, 2, 3], 4), [0, 2])
        self.assertEqual(two_sum([1234, 5678, 9012], 14690), [1, 2])
        self.assertEqual(two_sum([2, 2, 3], 4), [0, 1])

    def test_two_sum_second_solution(self):
        self.assertEqual(two_sum_second_solution([1, 2, 3], 4), [0, 2])
        self.assertEqual(two_sum_second_solution([1234, 5678, 9012], 14690), [1, 2])
        self.assertEqual(two_sum_second_solution([2, 2, 3], 4), [0, 1])
