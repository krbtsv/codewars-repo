import unittest

from katas.kyu_5.directions_reduction import (dir_reduc,
                                              dir_resuc_second_solution)


class DirReducTestCase(unittest.TestCase):
    def test_dir_reduc(self):
        self.assertEqual(dir_reduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']), ['WEST'])
        self.assertEqual(dir_reduc(['NORTH', 'WEST', 'SOUTH', 'EAST']), ['NORTH', 'WEST', 'SOUTH', 'EAST'])

    def test_dir_reduc_second_solution(self):
        self.assertEqual(dir_resuc_second_solution(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']),
                         ['WEST'])
        self.assertEqual(dir_resuc_second_solution(['NORTH', 'WEST', 'SOUTH', 'EAST']),
                         ['NORTH', 'WEST', 'SOUTH', 'EAST'])
