import unittest

from katas.kyu_7.shortest_word import find_short


class FindShortTestCase(unittest.TestCase):
    def test_find_short(self):
        self.assertEqual(find_short('bitcoin take over the world maybe who knows perhaps'), 3)
        self.assertEqual(find_short('i want to travel the world writing code one day'), 1)
        self.assertEqual(find_short('Lets all go on holiday somewhere very cold'), 2)
        self.assertEqual(find_short("Let's travel abroad shall we"), 2)
