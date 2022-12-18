import unittest
from katas.kyu_7.remove_the_minimum import remove_smallest, remove_smallest_second_solution


class RemoveSmallestTestCase(unittest.TestCase):
    def test_remove_smallest(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
        self.assertEqual(remove_smallest([]), [])

    def test_remove_smallest_second_solution(self):
        self.assertEqual(remove_smallest_second_solution([1, 2, 3, 4, 5]), [2, 3, 4, 5])
        self.assertEqual(remove_smallest_second_solution([5, 3, 2, 1, 4]), [5, 3, 2, 4])
        self.assertEqual(remove_smallest_second_solution([1, 2, 3, 1, 1]), [2, 3, 1, 1])
        self.assertEqual(remove_smallest_second_solution([]), [])
