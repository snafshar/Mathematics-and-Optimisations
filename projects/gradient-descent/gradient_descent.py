#!/usr/bin/env python3
"""Explore gradient descent on f(x) = (x - 3)^2 + 2."""

import argparse
import csv
from pathlib import Path


def objective(x: float) -> float:
    return (x - 3.0) ** 2 + 2.0


def gradient(x: float) -> float:
    return 2.0 * (x - 3.0)


def optimize(start: float, learning_rate: float, steps: int, tolerance: float):
    """Yield (iteration, x, f(x), gradient(x)) including the starting point."""
    x = start
    for iteration in range(steps + 1):
        grad = gradient(x)
        yield iteration, x, objective(x), grad
        if abs(grad) <= tolerance or iteration == steps:
            break
        x -= learning_rate * grad


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=float, default=-8.0)
    parser.add_argument("--learning-rate", type=float, default=0.1)
    parser.add_argument("--steps", type=int, default=25)
    parser.add_argument("--tolerance", type=float, default=1e-6)
    parser.add_argument("--csv", type=Path, default=None, help="optional path for iteration history")
    args = parser.parse_args()

    if not 0.0 < args.learning_rate < 1.0:
        parser.error("--learning-rate must be greater than 0 and less than 1 for this demo")
    if args.steps < 0:
        parser.error("--steps must be non-negative")
    if args.tolerance < 0:
        parser.error("--tolerance must be non-negative")

    history = list(optimize(args.start, args.learning_rate, args.steps, args.tolerance))
    print("iter        x             f(x)          gradient")
    for iteration, x, value, grad in history:
        print(f"{iteration:>4}  {x:>12.7f}  {value:>12.7f}  {grad:>12.7f}")

    final = history[-1]
    print(f"\nApproximate minimum: x={final[1]:.7f}, f(x)={final[2]:.7f}")
    if args.csv is not None:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["iteration", "x", "objective", "gradient"])
            writer.writerows(history)
        print(f"Saved iteration history to {args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
