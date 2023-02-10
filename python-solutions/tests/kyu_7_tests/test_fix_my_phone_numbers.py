import unittest

from katas.kyu_7.fix_my_phone_numbers import (is_it_a_num,
                                              is_it_a_num_second_solution)


class IsItANumTestCase(unittest.TestCase):
    def test_is_it_a_num(self):
        self.assertEqual(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
        self.assertEqual(is_it_a_num("sjfniebienvr12312312312ehfWh"), "Not a phone number")
        self.assertEqual(is_it_a_num("0192387415456"), "Not a phone number")
        self.assertEqual(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
        self.assertEqual(is_it_a_num("stop calling me no I have never been in an accident"), "Not a phone number")

    def test_is_it_a_num_second_solution(self):
        self.assertEqual(is_it_a_num_second_solution("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
        self.assertEqual(is_it_a_num_second_solution("sjfniebienvr12312312312ehfWh"), "Not a phone number")
        self.assertEqual(is_it_a_num_second_solution("0192387415456"), "Not a phone number")
        self.assertEqual(is_it_a_num_second_solution("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
        self.assertEqual(is_it_a_num_second_solution("stop calling me no I have never been in an accident"),
                         "Not a phone number")
