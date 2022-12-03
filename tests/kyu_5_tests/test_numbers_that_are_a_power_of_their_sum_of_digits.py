import unittest
from katas.kyu_5.numbers_that_are_a_power_of_their_sum_of_digits import power_sum_dig_term


class PowerSumDigTermTestCase(unittest.TestCase):
    def test_power_sum_dig_term(self):
        self.assertEqual(power_sum_dig_term(1), 81)
        self.assertEqual(power_sum_dig_term(2), 512)
        self.assertEqual(power_sum_dig_term(3), 2401)
        self.assertEqual(power_sum_dig_term(4), 4913)
        self.assertEqual(power_sum_dig_term(5), 5832)
