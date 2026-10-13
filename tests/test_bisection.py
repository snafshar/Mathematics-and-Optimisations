import unittest
from src.bisection import root


class BisectionTests(unittest.TestCase):
    def test_finds_square_root_of_two(self):
        result = root(lambda x: x * x - 2, 0, 2)
        self.assertAlmostEqual(result * result, 2, places=6)

    def test_endpoint_root(self):
        self.assertEqual(root(lambda x: x - 3, 3, 5), 3)

    def test_requires_sign_change(self):
        with self.assertRaises(ValueError):
            root(lambda x: x * x + 1, -1, 1)


if __name__ == "__main__":
    unittest.main()
