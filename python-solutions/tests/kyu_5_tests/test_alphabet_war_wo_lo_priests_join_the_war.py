import unittest

from katas.kyu_5.alphabet_war_wo_lo_priests_join_the_war import alphabet_war


class AlphabetWarTestCase(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war("z"), "Right side wins!")
        self.assertEqual(alphabet_war("jbdt"), "Let's fight again!")
        self.assertEqual(alphabet_war("jz"), "Right side wins!")
        self.assertEqual(alphabet_war("tzj"), "Right side wins!")
        self.assertEqual(alphabet_war("wololooooo"), "Left side wins!")
        self.assertEqual(alphabet_war("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war("ztztztzs"), "Left side wins!")


if __name__ == '__main__':
    unittest.main()
