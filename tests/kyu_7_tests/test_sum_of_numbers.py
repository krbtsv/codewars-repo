import unittest
from katas.kyu_7.sum_of_numbers import get_sum


class GetSumTestCase(unittest.TestCase):
    def test_get_sum(self):
        self.assertEqual(get_sum(0, 1), 1)
        self.assertEqual(get_sum(1, 0), 1)
        self.assertEqual(get_sum(1, 2), 3)
        self.assertEqual(get_sum(1, 1), 1)
        self.assertEqual(get_sum(-1, 0), -1)
        self.assertEqual(get_sum(-1, 2), 2)
