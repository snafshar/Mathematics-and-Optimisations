#!/usr/bin/env python3
"""Compare convergence of several learning rates for the demo quadratic."""

import argparse

from gradient_descent import objective, optimize


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=float, default=-8.0)
    parser.add_argument("--steps", type=int, default=25)
    parser.add_argument(
        "--rates",
        type=float,
        nargs="+",
        default=[0.01, 0.1, 0.5, 0.9],
        help="one or more learning rates in the interval (0, 1)",
    )
    args = parser.parse_args()

    if args.steps < 0:
        parser.error("--steps must be non-negative")
    if any(not 0.0 < rate < 1.0 for rate in args.rates):
        parser.error("every learning rate must be greater than 0 and less than 1")

    print(f"Start: x={args.start:g}; iteration limit: {args.steps}")
    print(f"{'rate':>10} {'iterations':>12} {'final x':>14} {'f(x)':>14} {'|gradient|':>14}")
    for rate in args.rates:
        history = list(optimize(args.start, rate, args.steps, tolerance=0.0))
        iteration, x, value, grad = history[-1]
        print(f"{rate:>10.4f} {iteration:>12d} {x:>14.7f} {value:>14.7f} {abs(grad):>14.7f}")

    print(f"Known minimum: x=3, f(x)={objective(3.0):g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
