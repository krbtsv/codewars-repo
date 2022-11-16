import unittest
from katas.kyu_7.mumbling import accum, accum_second_solution


class AccumTestCase(unittest.TestCase):
    def test_accum(self):
        self.assertEqual(accum('abcd'), 'A-Bb-Ccc-Dddd')
        self.assertEqual(accum('cwAt'), 'C-Ww-Aaa-Tttt')
        self.assertEqual(accum("ZpglnRxqenU"),
                         "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        self.assertEqual(accum_second_solution('Rtga'), 'R-Tt-Ggg-Aaaa')
