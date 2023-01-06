import unittest
from katas.kyu_6.counting_duplicates import duplicate_count, duplicate_count_second_solution


class DuplicateCountTestCase(unittest.TestCase):
    def test_duplicate_count(self):
        self.assertEqual(duplicate_count(''), 0)
        self.assertEqual(duplicate_count('abcde'), 0)
        self.assertEqual(duplicate_count('abcdeaa'), 1)
        self.assertEqual(duplicate_count('abcdeaB'), 2)
        self.assertEqual(duplicate_count('Indivisibilities'), 2)

    def test_duplicate_count_second_solution(self):
        self.assertEqual(duplicate_count_second_solution(''), 0)
        self.assertEqual(duplicate_count_second_solution('abcde'), 0)
        self.assertEqual(duplicate_count_second_solution('abcdeaa'), 1)
        self.assertEqual(duplicate_count_second_solution('abcdeaB'), 2)
        self.assertEqual(duplicate_count_second_solution('Indivisibilities'), 2)
