import unittest

from solution import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
        self.assertEqual(solution(l), ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])