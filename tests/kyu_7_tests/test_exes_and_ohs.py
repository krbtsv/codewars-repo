import unittest
from katas.kyu_7.exes_and_ohs import xo, xo_second_solution


class XoTestCase(unittest.TestCase):
    def test_xo(self):
        self.assertEqual(xo('xo'), True)
        self.assertEqual(xo('zzoo'), False)
        self.assertEqual(xo('xooxx'), False)
        self.assertEqual(xo('xoOxcvxcX'), False)
        self.assertEqual(xo('zpzpzp'), True)

    def test_xo_second_solution(self):
        self.assertEqual(xo_second_solution('zahdb'), True)
        self.assertEqual(xo_second_solution('xo'), True)
        self.assertEqual(xo_second_solution('XkjhxooXO'), True)
