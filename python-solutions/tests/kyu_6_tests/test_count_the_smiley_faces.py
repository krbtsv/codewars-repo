import unittest

from katas.kyu_6.count_the_smiley_faces import (count_smileys,
                                                count_smileys_second_solution,
                                                count_smileys_third_solution)


class CountSmileysTestCase(unittest.TestCase):
    def test_count_smileys(self):
        self.assertEqual(count_smileys([':D', ':~D', ';~D', ':)']), 4)
        self.assertEqual(count_smileys([':D', ':(', ';O', ':)']), 2)
        self.assertEqual(count_smileys([':]', ':[', ';*', ':)']), 1)

    def test_count_smileys_second_solution(self):
        self.assertEqual(count_smileys_second_solution([':D', ':~D', ';~D', ':)']), 4)
        self.assertEqual(count_smileys_second_solution([':D', ':(', ';O', ':)']), 2)
        self.assertEqual(count_smileys_second_solution([':]', ':[', ';*', ':)']), 1)

    def test_count_smileys_third_solution(self):
        self.assertEqual(count_smileys_third_solution([':D', ':~D', ';~D', ':)']), 4)
        self.assertEqual(count_smileys_third_solution([':D', ':(', ';O', ':)']), 2)
        self.assertEqual(count_smileys_third_solution([':]', ':[', ';*', ':)']), 1)
