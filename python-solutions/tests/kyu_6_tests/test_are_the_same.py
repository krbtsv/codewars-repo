import unittest

from katas.kyu_6.are_they_the_same import comp


class CompTestCase(unittest.TestCase):
    def test_comp(self):
        self.assertEqual(comp(
            [121, 144, 19, 161, 19, 144, 19, 11],
            [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        ), True)

        self.assertEqual(comp(
            [121, 144, 19, 161, 19, 144, 19, 11],
            [231, 14641, 20736, 361, 25921, 361, 20736, 361]
        ), False)

        self.assertEqual(comp(
            [],
            [231, 14641, 20736, 361, 25921, 361, 20736, 361]
        ), False)

        self.assertEqual(comp(
            [1, 3, 45, 65, 64, 4, 111],
            [231, 14641, 20736, 361, 25921, 361, 20736, 361]
        ), False)
