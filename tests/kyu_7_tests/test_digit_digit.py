import unittest

from katas.kyu_7.digit_digit import square_digits


class SquareDigitsTestCase(unittest.TestCase):
    def test_square_digits(self):
        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(112), 114)
        self.assertEqual(square_digits(765), 493625)
        self.assertEqual(square_digits(0), 0)
