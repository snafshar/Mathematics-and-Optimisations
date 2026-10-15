# Gradient Descent Lab

A compact, dependency-free Python project that demonstrates gradient descent on a one-dimensional quadratic function:

    f(x) = (x - 3)^2 + 2

Its minimum is at x = 3. The script records each iteration so you can inspect how the learning rate affects convergence.

## Run

    python gradient_descent.py
    python gradient_descent.py --start -8 --learning-rate 0.1 --steps 25

Python 3.10+ is recommended. No third-party packages are required.

## Topics

- Objective functions and derivatives
- Iterative optimization
- Learning rate and convergence
- Stopping criteria and numerical stability
- CSV output for plotting in another tool

## Experiments

1. Try learning rates 0.01, 0.1, 0.5, and 1.1.
2. Start from positive and negative initial values.
3. Compare fixed iteration count with a gradient tolerance.
4. Generalize the implementation to a vector and a quadratic form.
