import unittest

from katas.kyu_6.the_supermarket_queue import queue_time


class QueueTimeTestCase(unittest.TestCase):
    def test_queue_time(self):
        self.assertEqual(queue_time([2, 2, 3, 3, 4, 4], 2), 9)
        self.assertEqual(queue_time([1, 2, 3, 5], 100), 5)
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 1), 15)
        self.assertEqual(queue_time([2], 5), 2)
        self.assertEqual(queue_time([5], 1), 5)
        self.assertEqual(queue_time([], 1), 0)
