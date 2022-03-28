from unittest import TestCase
import numpy as np
from test_environment import TestEnvironment


class TestTestEnvironment(TestCase):
    def setUp(self) -> None:
        self.env = TestEnvironment()


class TestInit(TestTestEnvironment):
    def test_initial_transform(self):
        self.assertSequenceEqual(self.env.local, ([0]))


# noinspection PyTypeChecker
class TestNavigation(TestTestEnvironment):
    def test_check_1(self):
        self.env.transform_coordinate([0.30, 1.50], 1)
        self.assertSequenceEqual(np.around(self.env.local, 2).tolist(), [0, 0])

    def test_check_2(self):
        self.env.transform_coordinate([0.90, 1.50], 2)
        self.assertSequenceEqual(np.around(self.env.local, 2).tolist(), [0, 0])

    def test_check_3(self):
        self.env.transform_coordinate([2.10, 0.90], 6)
        self.assertSequenceEqual(np.around(self.env.local, 2).tolist(), [0, 0])

    def test_check_4(self):
        self.env.transform_coordinate([0.40, 1.0], 3)
        self.assertSequenceEqual(np.around(self.env.local, 2).tolist(), [0.1, 0.1])

    def test_check_5(self):
        self.env.transform_coordinate([1.90, 0.20], 8)
        self.assertSequenceEqual(np.around(self.env.local, 2).tolist(), [-0.2, -0.1])
