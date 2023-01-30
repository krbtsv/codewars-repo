import unittest

from katas.kyu_6.perfect_square import perfect_square


class PerfectSquareTestCase(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(perfect_square('.'), True)
        self.assertEqual(perfect_square('..\n..'), True)
        self.assertEqual(perfect_square('...\n...\n...'), True)
        self.assertEqual(perfect_square('+'), False)
        self.assertEqual(perfect_square('...\n.:.\n...'), False)
        self.assertEqual(perfect_square('---\n---\n---'), False)
        self.assertEqual(perfect_square('..'), False)
        self.assertEqual(perfect_square('.\n.\n.'), False)
        self.assertEqual(perfect_square('...\n....\n...'), False)
        self.assertEqual(perfect_square('...\n..\n...'), False)
