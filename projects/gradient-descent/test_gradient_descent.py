"""Tests for the gradient descent demonstration."""

import unittest

from gradient_descent import gradient, objective, optimize


class GradientDescentTests(unittest.TestCase):
    def test_known_minimum(self):
        self.assertAlmostEqual(objective(3.0), 2.0)
        self.assertAlmostEqual(gradient(3.0), 0.0)

    def test_objective_is_nonnegative(self):
        for value in (-10.0, -1.0, 0.0, 3.0, 12.0):
            self.assertGreaterEqual(objective(value), 2.0)

    def test_optimizer_moves_towards_minimum(self):
        history = list(optimize(-8.0, 0.1, 25, 0.0))
        self.assertLess(abs(history[-1][1] - 3.0), abs(history[0][1] - 3.0))

    def test_optimizer_includes_initial_point(self):
        history = list(optimize(7.0, 0.1, 0, 0.0))
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0][1], 7.0)


if __name__ == "__main__":
    unittest.main()
