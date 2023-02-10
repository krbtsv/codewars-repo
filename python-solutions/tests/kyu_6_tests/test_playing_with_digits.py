import unittest

from katas.kyu_6.playing_with_digits import dig_pow, dig_pow_second_solution


class DigPowTestCase(unittest.TestCase):
    def test_dig_pow(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(695, 2), 2)
        self.assertEqual(dig_pow(46288, 3), 51)

    def test_dig_pow_second_solution(self):
        self.assertEqual(dig_pow_second_solution(89, 1), 1)
        self.assertEqual(dig_pow_second_solution(92, 1), -1)
        self.assertEqual(dig_pow_second_solution(695, 2), 2)
        self.assertEqual(dig_pow_second_solution(46288, 3), 51)
