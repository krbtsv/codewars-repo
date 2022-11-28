import unittest
from katas.kyu_7.get_the_middle_character import get_middle


class GetMiddleTestCase(unittest.TestCase):
    def test_get_middle(self):
        self.assertEqual(get_middle('test'), 'es')
        self.assertEqual(get_middle('testing'), 't')
        self.assertEqual(get_middle('middle'), 'dd')
        self.assertEqual(get_middle('A'), 'A')
        self.assertEqual(get_middle('of'), 'of')
