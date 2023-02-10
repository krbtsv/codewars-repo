import unittest

from katas.kyu_6.alphabet_war_airstrike_letters_massacre import (
    alphabet_war, alphabet_war_second_solution)


class AlphabetWarTestCase(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war("z"), "Right side wins!")
        self.assertEqual(alphabet_war("****"), "Let's fight again!")
        self.assertEqual(alphabet_war("z*dq*mw*pb*s"), "Let's fight again!")
        self.assertEqual(alphabet_war("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war("zz*zzs"), "Right side wins!")
        self.assertEqual(alphabet_war("sz**z**zs"), "Left side wins!")
        self.assertEqual(alphabet_war("z*z*z*zs"), "Left side wins!")
        self.assertEqual(alphabet_war("*wwwwww*z*"), "Left side wins!")
        self.assertEqual(alphabet_war("w****z"), "Let's fight again!")
        self.assertEqual(alphabet_war("mb**qwwp**dm"), "Let's fight again!")

    def test_alphabet_war_second_solution(self):
        self.assertEqual(alphabet_war_second_solution("z"), "Right side wins!")
        self.assertEqual(alphabet_war_second_solution("****"), "Let's fight again!")
        self.assertEqual(alphabet_war_second_solution("z*dq*mw*pb*s"), "Let's fight again!")
        self.assertEqual(alphabet_war_second_solution("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war_second_solution("zz*zzs"), "Right side wins!")
        self.assertEqual(alphabet_war_second_solution("sz**z**zs"), "Left side wins!")
        self.assertEqual(alphabet_war_second_solution("z*z*z*zs"), "Left side wins!")
        self.assertEqual(alphabet_war_second_solution("*wwwwww*z*"), "Left side wins!")
        self.assertEqual(alphabet_war_second_solution("w****z"), "Let's fight again!")
        self.assertEqual(alphabet_war_second_solution("mb**qwwp**dm"), "Let's fight again!")
