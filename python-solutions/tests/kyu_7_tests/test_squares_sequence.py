import unittest

from katas.kyu_7.squares_sequence import squares

class FindSquares(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(squares([2, 5]), [2, 4, 16, 256, 65536])
        self.assertEqual(squares([3, 3]), [3, 9, 81])
        self.assertEqual(squares([1, -1]), [])
        self.assertEqual(squares([1, 0]), [])