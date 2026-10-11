"""Central finite-difference approximation for a scalar function."""


def derivative(function, x: float, step: float = 1e-5) -> float:
    if step <= 0:
        raise ValueError("step must be positive")
    return (function(x + step) - function(x - step)) / (2 * step)


if __name__ == "__main__":
    print(derivative(lambda value: value * value, 3.0))
