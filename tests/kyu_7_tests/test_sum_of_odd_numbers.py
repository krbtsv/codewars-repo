import unittest
from katas.kyu_7.sum_of_odd_numbers import row_sum_odd_numbers


class RowSumOddNumbersTestCase(unittest.TestCase):
    def test_row_sum_odd_numbers(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)
