import unittest

from katas.kyu_7.sum_of_the_first_nth_terms_of_series import series_sum


class SeriesSumTestCase(unittest.TestCase):
    def test_series_sum(self):
        self.assertEqual(series_sum(1), '1.00')
        self.assertEqual(series_sum(2), '1.25')
        self.assertEqual(series_sum(3), '1.39')
        self.assertEqual(series_sum(0), '0.00')
        self.assertEqual(series_sum(5), '1.57')
