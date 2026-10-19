"""Compare final objective values and runtime for optimization routines."""

import argparse
import time

from coordinate_descent import coordinate_descent
from gradient_descent_2d import minimize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", nargs="+", type=int, default=[10, 50, 200])
    args = parser.parse_args()
    if any(value < 0 for value in args.steps):
        parser.error("all step counts must be non-negative")
    print(f"{'steps':>8} {'method':>14} {'seconds':>12} {'final f':>14}")
    for steps in args.steps:
        for name, function in (("coordinate", coordinate_descent), ("gradient", minimize)):
            started = time.perf_counter()
            history = function(iterations=steps) if name == "coordinate" else function(max_iterations=steps)
            elapsed = time.perf_counter() - started
            print(f"{steps:8d} {name:>14s} {elapsed:12.6f} {history[-1][3]:14.8f}")


if __name__ == "__main__":
    main()
