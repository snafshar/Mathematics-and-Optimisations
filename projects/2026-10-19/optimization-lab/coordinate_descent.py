"""Exact coordinate updates for a simple two-variable quadratic."""


def objective(point):
    x, y = point
    return 2 * x * x + x * y + y * y - 6 * x - 5 * y


def coordinate_descent(start=(0.0, 0.0), iterations=50):
    """Return the full history for exact coordinate updates.

    For this objective, minimizing one coordinate at a time gives:
      x <- (6 - y) / 4
      y <- (5 - x) / 2
    """
    if iterations < 0:
        raise ValueError("iterations must be non-negative")
    x, y = float(start[0]), float(start[1])
    history = [(0, x, y, objective((x, y)))]
    for step in range(1, iterations + 1):
        x = (6.0 - y) / 4.0
        y = (5.0 - x) / 2.0
        history.append((step, x, y, objective((x, y))))
    return history
