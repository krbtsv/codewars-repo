import unittest
from katas.kyu_7.sum_of_two_lowest_positive_integers import sum_of_two_smallest_numbers


class SumOfTwoSmallestNumbersTestCase(unittest.TestCase):
    def test_sum_of_two_smallest_numbers(self):
        self.assertEqual(sum_of_two_smallest_numbers([1, 2, 3, 3, 10, 11]), 3)
        self.assertEqual(sum_of_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        self.assertEqual(sum_of_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        self.assertEqual(sum_of_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
