from katas.kyu_5.moving_zeroes_to_the_end import move_zero
import unittest


class MoveZeroTestCase(unittest.TestCase):
    def test_zero_move_end(self):
        self.assertEqual(move_zero([1, 2, 5, 0, 11, 0, -1]), [1, 2, 5, 11, -1, 0, 0])
        self.assertEqual(move_zero([12, 'lek', True, 0, 11, (1, 1), False, 0, 17, 0]),
                         [12, 'lek', True, 11, (1, 1), False, 17, 0, 0, 0])

    def test_types(self):
        self.assertRaises(TypeError, move_zero, 4)
        self.assertRaises(TypeError, move_zero, 'lol')
        self.assertRaises(TypeError, move_zero, False)
        self.assertRaises(TypeError, move_zero, (1, 2))
        self.assertRaises(TypeError, move_zero, {0, 10, 1})
