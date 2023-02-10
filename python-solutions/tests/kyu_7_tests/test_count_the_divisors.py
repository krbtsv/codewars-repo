import unittest

from katas.kyu_7.count_the_divisors import divisors


class DivisorsTestCase(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(1), 1)
        self.assertEqual(divisors(4), 3)
        self.assertEqual(divisors(5), 2)
        self.assertEqual(divisors(12), 6)
        self.assertEqual(divisors(30), 8)
        self.assertEqual(divisors(4096), 13)
