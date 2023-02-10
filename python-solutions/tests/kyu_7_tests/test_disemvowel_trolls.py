import unittest

from katas.kyu_7.disemvowel_trolls import (disemvowel,
                                           disemvowel_second_solution,
                                           disemvowel_third_solution)


class DisemvowelTestCase(unittest.TestCase):
    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

    def test_disemvowel_second_solution(self):
        self.assertEqual(disemvowel_second_solution("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

    def test_disemvowel_third_solution(self):
        self.assertEqual(disemvowel_third_solution("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
