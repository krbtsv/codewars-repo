import unittest

from katas.kyu_6.write_number_in_expanded_form import (
    expanded_form, expanded_form_second_solution)


class ExpendedFormTestCase(unittest.TestCase):
    def test_expended_form(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')

    def test_expended_form_second_solution(self):
        self.assertEqual(expanded_form_second_solution(12), '10 + 2')
        self.assertEqual(expanded_form_second_solution(44), '40 + 4')
        self.assertEqual(expanded_form_second_solution(78380), '70000 + 8000 + 300 + 80')
