import unittest

from katas.kyu_6.bouncing_balls import (bouncing_ball,
                                        bouncing_ball_second_solution)


class BouncingBallTestCase(unittest.TestCase):
    def test_bouncing_ball(self):
        self.assertEqual(bouncing_ball(2, 0.5, 1), 1)
        self.assertEqual(bouncing_ball(3, 0.66, 1.5), 3)
        self.assertEqual(bouncing_ball(30, 0.66, 1.5), 15)
        self.assertEqual(bouncing_ball(30, 0.75, 1.5), 21)
        self.assertEqual(bouncing_ball(0, 0.75, 1.5), -1)
        self.assertEqual(bouncing_ball(30, 1.5, 1.5), -1)
        self.assertEqual(bouncing_ball(0.75, 0.75, 0.75), -1)

    def test_bouncing_ball_second_solution(self):
        self.assertEqual(bouncing_ball_second_solution(2, 0.5, 1), 1)
        self.assertEqual(bouncing_ball_second_solution(3, 0.66, 1.5), 3)
        self.assertEqual(bouncing_ball_second_solution(30, 0.66, 1.5), 15)
        self.assertEqual(bouncing_ball_second_solution(30, 0.75, 1.5), 21)
        self.assertEqual(bouncing_ball_second_solution(0, 0.75, 1.5), -1)
        self.assertEqual(bouncing_ball_second_solution(30, 1.5, 1.5), -1)
        self.assertEqual(bouncing_ball_second_solution(0.75, 0.75, 0.75), -1)
