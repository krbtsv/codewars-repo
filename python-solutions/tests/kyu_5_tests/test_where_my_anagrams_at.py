import unittest

from katas.kyu_5.where_my_anagrams_at import anagrams, anagrams_second_solution


class AnagramsTestCase(unittest.TestCase):
    def test_anagrams(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEqual(anagrams('laser', ['lazing', 'lazy', 'lacer']), [])
        self.assertEqual(anagrams('a', ['a', 'b', 'c', 'd']), ['a'])
        self.assertEqual(anagrams('big', ['gig', 'dib', 'bid', 'biig']), [])
        self.assertEqual(anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']), ['ab', 'ba'])
        self.assertEqual(anagrams('abba',
                                  ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab',
                                   'abbab', 'abbaa', 'babaa']), ['aabb', 'bbaa', 'abab', 'baba', 'baab'])

    def test_anagrams_second_solution(self):
        self.assertEqual(anagrams_second_solution('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams_second_solution('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']),
                         ['carer', 'racer'])
        self.assertEqual(anagrams_second_solution('laser', ['lazing', 'lazy', 'lacer']), [])
        self.assertEqual(anagrams_second_solution('a', ['a', 'b', 'c', 'd']), ['a'])
        self.assertEqual(anagrams_second_solution('big', ['gig', 'dib', 'bid', 'biig']), [])
        self.assertEqual(
            anagrams_second_solution('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']),
            ['ab', 'ba'])
        self.assertEqual(anagrams_second_solution('abba',
                                                  ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd',
                                                   'abbba', 'baaab',
                                                   'abbab', 'abbaa', 'babaa']),
                         ['aabb', 'bbaa', 'abab', 'baba', 'baab'])
