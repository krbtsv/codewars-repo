import unittest
from katas.kyu_6.your_order_please import order, order_second_solution


class OrderTestCase(unittest.TestCase):
    def test_order(self):
        self.assertEqual(order('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')
        self.assertEqual(order('4of Fo1r pe6ople g3ood th5e the2'), 'Fo1r the2 g3ood 4of th5e pe6ople')
        self.assertEqual(order(''), '')

    def test_order_second_solution(self):
        self.assertEqual(order_second_solution('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')
        self.assertEqual(order_second_solution('4of Fo1r pe6ople g3ood th5e the2'), 'Fo1r the2 g3ood 4of th5e pe6ople')
        self.assertEqual(order_second_solution(''), '')
