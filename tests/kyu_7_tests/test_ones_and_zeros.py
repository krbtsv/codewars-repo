import unittest
from katas.kyu_7.ones_and_zeros import binary_array_to_number


class BinaryArrayToNumberTestCase(unittest.TestCase):
    def test_binary_array_to_number(self):
        self.assertEqual(binary_array_to_number([0, 0, 0, 1]), 1)
        self.assertEqual(binary_array_to_number([0, 0, 1, 0]), 2)
        self.assertEqual(binary_array_to_number([1, 1, 1, 1]), 15)
        self.assertEqual(binary_array_to_number([1, 0, 1, 1]), 11)
        self.assertEqual(binary_array_to_number([0, 1, 1, 0]), 6)
        self.assertEqual(binary_array_to_number([1, 0, 0, 1]), 9)
