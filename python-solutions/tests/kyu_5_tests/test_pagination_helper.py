import unittest

from katas.kyu_5.pagination_helper import PaginationHelper


class PaginationHelperTestCase(unittest.TestCase):
    COLLECTIONS = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    ITEMS_PER_PAGE = 5

    def test_pagination_helper_method(self):
        helper = PaginationHelper(self.COLLECTIONS, self.ITEMS_PER_PAGE)
        self.assertEqual(helper.page_count(), 3)
        self.assertEqual(helper.item_count(), 14)
        self.assertEqual(helper.page_item_count(0), 5)
        self.assertEqual(helper.page_item_count(1), 5)
        self.assertEqual(helper.page_item_count(2), 4)
        self.assertEqual(helper.page_item_count(3), -1)
        self.assertEqual(helper.page_index(5), 1)
        self.assertEqual(helper.page_index(2), 0)
        self.assertEqual(helper.page_index(9), 1)
        self.assertEqual(helper.page_index(10), 2)
        self.assertEqual(helper.page_index(11), 2)
        self.assertEqual(helper.page_index(20), -1)
        self.assertEqual(helper.page_index(-10), -1)
