from katas.kyu_5.calculating_with_functions import *
import unittest


class CalculatingTestCase(unittest.TestCase):
    def test_calculating(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)
        self.assertEqual(four(divided_by(three())), 1)
        self.assertEqual(five(divided_by(two())), 2)
