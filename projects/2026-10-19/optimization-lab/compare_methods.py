"""Compare coordinate descent and gradient descent on the same objective."""

import argparse

from coordinate_descent import coordinate_descent
from gradient_descent_2d import minimize, objective


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=50)
    parser.add_argument("--start-x", type=float, default=0.0)
    parser.add_argument("--start-y", type=float, default=0.0)
    args = parser.parse_args()
    if args.steps < 0:
        parser.error("--steps must be non-negative")

    start = (args.start_x, args.start_y)
    coordinate = coordinate_descent(start, args.steps)
    gradient = minimize(start, args.steps)
    for name, history in (("coordinate", coordinate), ("gradient", gradient)):
        _, x, y, value = history[-1][:4]
        print(f"{name:10s} iterations={history[-1][0]:3d} x={x:.8f} y={y:.8f} f={value:.8f}")
    print(f"Known solution: x=1, y=2, f={objective((1, 2)):.8f}")


if __name__ == "__main__":
    main()
