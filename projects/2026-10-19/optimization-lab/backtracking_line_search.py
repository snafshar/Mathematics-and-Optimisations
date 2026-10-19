"""A small Armijo backtracking line search for vector-valued points."""


def dot(first, second):
    return sum(a * b for a, b in zip(first, second))


def add_scaled(point, direction, scale):
    return [value + scale * delta for value, delta in zip(point, direction)]


def armijo_backtracking(objective, gradient, point, direction,
                        initial_step=1.0, shrink=0.5, sufficient_decrease=1e-4,
                        min_step=1e-12):
    """Return a step length satisfying the Armijo sufficient-decrease rule."""
    if not 0 < shrink < 1:
        raise ValueError("shrink must be in (0, 1)")
    if not 0 < sufficient_decrease < 1:
        raise ValueError("sufficient_decrease must be in (0, 1)")
    if initial_step <= 0 or min_step <= 0:
        raise ValueError("step lengths must be positive")
    slope = dot(gradient(point), direction)
    if slope >= 0:
        raise ValueError("direction must be a descent direction")
    current_value = objective(point)
    step = initial_step
    while step >= min_step:
        candidate = add_scaled(point, direction, step)
        if objective(candidate) <= current_value + sufficient_decrease * step * slope:
            return step
        step *= shrink
    return min_step
