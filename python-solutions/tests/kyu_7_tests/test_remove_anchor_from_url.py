import unittest

from katas.kyu_7.remove_anchor_from_url import (
    remove_url_anchor, remove_url_anchor_second_solution)


class RemoveUrlAnchorTestCase(unittest.TestCase):
    def test_remove_url_anchor(self):
        self.assertEqual(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")

    def test_remove_url_anchor_second_solution(self):
        self.assertEqual(remove_url_anchor_second_solution("www.codewars.com#about"), "www.codewars.com")
        self.assertEqual(remove_url_anchor_second_solution("www.codewars.com/katas/?page=1#about"),
                         "www.codewars.com/katas/?page=1")
        self.assertEqual(remove_url_anchor_second_solution("www.codewars.com/katas/"), "www.codewars.com/katas/")
