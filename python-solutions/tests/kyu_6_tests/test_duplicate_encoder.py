import unittest

from katas.kyu_6.duplicate_encoder import duplicate_encode


class DuplicateEncodeTestCase(unittest.TestCase):
    def test_duplicate_encode(self):
        self.assertEqual(duplicate_encode('din'), '(((')
        self.assertEqual(duplicate_encode('recede'), '()()()')
        self.assertEqual(duplicate_encode('Success'), ')())())')
        self.assertEqual(duplicate_encode('(( @'), '))((')
        self.assertEqual(duplicate_encode('aba  bb'), ')))))))')
