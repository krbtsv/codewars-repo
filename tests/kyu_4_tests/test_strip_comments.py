import unittest
from katas.kyu_4.strip_comments import strip_comments


class StripCommentsTestCase(unittest.TestCase):
    def test_strip_comments(self):
        string = 'apples, pears # and bananas\ngrapes\nwatermelon !cherry'
        markers = ['#', '!']
        result = strip_comments(string, markers)
        string = ' a #b\nc\nd $e f g'
        markers = ['#', '$']
        result2 = strip_comments(string, markers)
        self.assertEqual(result, 'apples, pears\ngrapes\nwatermelon')
        self.assertEqual(result2, ' a\nc\nd')

    def test_correct_values(self):
        string = "\tlemons strawberries\n# pears\n- oranges cherries bananas\n? .strawberries avocados pears '\n."
        markers = []
        result = strip_comments(string, markers)
        self.assertEqual(result, string)