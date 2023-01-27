import unittest

from katas.kyu_8.regex_basics_is_it_a_digit import is_digit, is_digit_second_solution


class IsDigitTestCase(unittest.TestCase):
    def test_is_digit(self):
        self.assertEqual(is_digit(""), False)
        self.assertEqual(is_digit("7"), True)
        self.assertEqual(is_digit(" "), False)
        self.assertEqual(is_digit("a"), False)
        self.assertEqual(is_digit("a5"), False)

    def test_is_digit_second_solution(self):
        self.assertEqual(is_digit_second_solution(""), False)
        self.assertEqual(is_digit_second_solution("7"), True)
        self.assertEqual(is_digit_second_solution(" "), False)
        self.assertEqual(is_digit_second_solution("a"), False)
        self.assertEqual(is_digit_second_solution("a5"), False)
