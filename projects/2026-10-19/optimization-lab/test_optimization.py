import unittest

from backtracking_line_search import armijo_backtracking
from coordinate_descent import coordinate_descent, objective
from gradient_descent_2d import gradient, minimize


class OptimizationTests(unittest.TestCase):
    def test_coordinate_descent_converges(self):
        history = coordinate_descent(iterations=20)
        _, x, y, value = history[-1]
        self.assertAlmostEqual(x, 1.0, places=5)
        self.assertAlmostEqual(y, 2.0, places=5)
        self.assertAlmostEqual(value, -8.0, places=5)

    def test_gradient_descent_reduces_objective(self):
        history = minimize(max_iterations=100)
        self.assertLess(history[-1][3], history[0][3])
        self.assertAlmostEqual(history[-1][1], 1.0, places=4)
        self.assertAlmostEqual(history[-1][2], 2.0, places=4)

    def test_armijo_step_is_positive_and_decreases(self):
        point = [0.0, 0.0]
        grad = gradient(point)
        direction = [-value for value in grad]
        step = armijo_backtracking(objective, gradient, point, direction)
        self.assertGreater(step, 0.0)
        candidate = [point[i] + step * direction[i] for i in range(2)]
        self.assertLess(objective(candidate), objective(point))

    def test_invalid_direction_is_rejected(self):
        with self.assertRaises(ValueError):
            armijo_backtracking(objective, gradient, [0, 0], [1, 1])


if __name__ == "__main__":
    unittest.main()
