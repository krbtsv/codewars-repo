import unittest

from katas.kyu_5.alphabet_wars_nuclear_strike import alphabet_war


class AlphabetWarTestCase(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war('[a]#[b]#[c]'), 'ac')
        self.assertEqual(alphabet_war('[a]#b#[c][d]'), 'd')
        self.assertEqual(alphabet_war('[a][b][c]'), 'abc')
        self.assertEqual(alphabet_war('##a[a]b[c]#'), 'c')
        self.assertEqual(alphabet_war('abde[fgh]ijk'), 'abdefghijk')
        self.assertEqual(alphabet_war('ab#de[fgh]ijk'), 'fgh')
        self.assertEqual(alphabet_war('ab#de[fgh]ij#k'), '')
        self.assertEqual(alphabet_war('##abde[fgh]ijk'), '')
        self.assertEqual(alphabet_war('##abde[fgh]'), '')
        self.assertEqual(alphabet_war('##abcde[fgh]'), '')
        self.assertEqual(alphabet_war('abcde[fgh]'), 'abcdefgh')
        self.assertEqual(alphabet_war('##abde[fgh]ijk[mn]op'), 'mn')
        self.assertEqual(alphabet_war('#abde[fgh]i#jk[mn]op'), 'mn')
        self.assertEqual(alphabet_war('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#'), 'abijk')
