import unittest
from katas.kyu_7.growth_of_a_population import nb_year, nb_year_second_solution


class NbYearsTestCase(unittest.TestCase):
    def test_nb_year(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)
        self.assertEqual(nb_year(1000, 2, 50, 1200), 3)

    def test_nb_years_second_solution(self):
        self.assertEqual(nb_year_second_solution(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year_second_solution(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year_second_solution(1500000, 0.25, 1000, 2000000), 94)
        self.assertEqual(nb_year_second_solution(1000, 2, 50, 1200), 3)
