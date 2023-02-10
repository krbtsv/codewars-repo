import unittest

from katas.kyu_6.find_the_odd_int import find_it


class FindItTestCase(unittest.TestCase):
    def test_find_it(self):
        self.assertEqual(find_it([20, 1, -1, 20, 1, -1, 3]), 3)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([10, 10, 10]), 10)
