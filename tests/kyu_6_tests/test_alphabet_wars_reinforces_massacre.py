import unittest

from katas.kyu_6.alphabet_wars_reinforces_massacre import alphabet_war

reinforces = ["g964xxxxxxxx",
              "myjinxin2015",
              "steffenvogel",
              "smile67xxxxx",
              "giacomosorbi",
              "freywarxxxxx",
              "bkaesxxxxxxx",
              "vadimbxxxxxx",
              "zozofouchtra",
              "colbydauphxx"]
airstrikes = ["* *** ** ***",
              " ** * * * **",
              " * *** * ***",
              " **  * * ** ",
              "* ** *   ***",
              "***   ",
              "**",
              "*",
              "*"]


class AlphabetWarTestCase(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war(reinforces, airstrikes), 'codewarsxxxx');
        self.assertEqual(alphabet_war(["abcdefg", "hijklmn"], ["   *   ", "*  *   "]), 'hi___fg');
        self.assertEqual(alphabet_war(["aaaaa", "bbbbb", "ccccc", "ddddd"], ["*", " *", "   "]), 'ccbaa');
