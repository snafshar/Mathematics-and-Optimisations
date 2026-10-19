# Optimization Lab

A dependency-free Python lab for comparing coordinate descent and gradient descent on a two-variable strictly convex quadratic.

The demo objective is

`f(x, y) = 2x² + xy + y² - 6x - 5y`

Its unique minimum is at `(1, 2)`. The example is small enough to verify analytically and still demonstrates update order, gradient direction, and line search.

## Run

```bash
cd projects/2026-10-19/optimization-lab
python compare_methods.py
python -m unittest discover -v
python benchmark_optimization.py --steps 10 50 200
```

The benchmark reports iteration counts and objective values rather than making claims about universal performance. CI runs the unit tests using supported Python versions.
