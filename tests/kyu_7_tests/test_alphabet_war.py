import unittest

from katas.kyu_7.alphabet_war import alphabet_war, alphabet_war_second_solution


class AlphabetWarTestCase(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war("z"), "Right side wins!")
        self.assertEqual(alphabet_war("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war("wq"), "Left side wins!")
        self.assertEqual(alphabet_war("zzzzs"), "Right side wins!")
        self.assertEqual(alphabet_war("wwwwww"), "Left side wins!")

    def test_alphabet_war_second_solution(self):
        self.assertEqual(alphabet_war_second_solution("z"), "Right side wins!")
        self.assertEqual(alphabet_war_second_solution(
            "zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war_second_solution("wq"), "Left side wins!")
        self.assertEqual(alphabet_war_second_solution("zzzzs"), "Right side wins!")
        self.assertEqual(alphabet_war_second_solution("wwwwww"), "Left side wins!")
