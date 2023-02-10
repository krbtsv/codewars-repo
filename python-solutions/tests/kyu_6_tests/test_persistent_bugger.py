import unittest

from katas.kyu_6.persistent_bugger import (persistence,
                                           persistence_second_solution)


class PersistenceTestCase(unittest.TestCase):
    def test_persistence(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(999), 4)
        self.assertEqual(persistence(25), 2)

    def test_persistence_second_solution(self):
        self.assertEqual(persistence_second_solution(39), 3)
        self.assertEqual(persistence_second_solution(4), 0)
        self.assertEqual(persistence_second_solution(999), 4)
        self.assertEqual(persistence_second_solution(25), 2)
