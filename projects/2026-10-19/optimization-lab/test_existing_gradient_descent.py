import sys
import unittest
from pathlib import Path

# The original implementation is maintained in a sibling project folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "gradient-descent"))

from gradient_descent import gradient, objective, optimize


class ExistingGradientDescentTests(unittest.TestCase):
    def test_known_minimum(self):
        self.assertEqual(objective(3.0), 2.0)
        self.assertEqual(gradient(3.0), 0.0)

    def test_iteration_history_includes_start(self):
        history = list(optimize(-8.0, 0.1, 5, tolerance=0.0))
        self.assertEqual(history[0][0], 0)
        self.assertEqual(history[-1][0], 5)
        self.assertLess(abs(history[-1][1] - 3.0), abs(history[0][1] - 3.0))

    def test_zero_steps_returns_initial_state(self):
        history = list(optimize(4.0, 0.1, 0, tolerance=0.0))
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0][1], 4.0)


if __name__ == "__main__":
    unittest.main()
