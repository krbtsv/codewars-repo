import unittest

from katas.kyu_7.descending_order import descending_order


class DescendingOrderTestCase(unittest.TestCase):
    def test_descending_order(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(15), 51)
        self.assertEqual(descending_order(42145), 54421)
        self.assertEqual(descending_order(145263), 654321)
        self.assertEqual(descending_order(123456789), 987654321)
