import unittest

from katas.kyu_5.maximum_subarray_sum import (
    max_sequence, max_sequence_perfect_solution, max_sequence_second_solution,
    max_sequence_simple_fast_solution)


class MaxSequenceTestCase(unittest.TestCase):
    def test_max_sequence(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1]), 0)
        self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)

    def test_max_sequence_second_solution(self):
        self.assertEqual(max_sequence_second_solution([]), 0)
        self.assertEqual(max_sequence_second_solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence_second_solution([-2, -1, -3, -4, -1, -2, -1]), 0)
        self.assertEqual(max_sequence_second_solution([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)

    def test_max_sequence_perfect_solution(self):
        self.assertEqual(max_sequence_perfect_solution([]), 0)
        self.assertEqual(max_sequence_perfect_solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence_perfect_solution([-2, -1, -3, -4, -1, -2, -1]), 0)
        self.assertEqual(max_sequence_perfect_solution([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)

    def test_max_sequence_simple_fast_solution(self):
        self.assertEqual(max_sequence_simple_fast_solution([]), 0)
        self.assertEqual(max_sequence_simple_fast_solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence_simple_fast_solution([-2, -1, -3, -4, -1, -2, -1]), 0)
        self.assertEqual(max_sequence_simple_fast_solution([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)
