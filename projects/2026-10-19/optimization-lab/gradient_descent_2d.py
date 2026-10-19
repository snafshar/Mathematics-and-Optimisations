"""Gradient descent on the two-dimensional quadratic used in this lab."""


from backtracking_line_search import add_scaled, armijo_backtracking


def objective(point):
    x, y = point
    return 2 * x * x + x * y + y * y - 6 * x - 5 * y


def gradient(point):
    x, y = point
    return [4 * x + y - 6, x + 2 * y - 5]


def minimize(start=(0.0, 0.0), max_iterations=100, tolerance=1e-8):
    if max_iterations < 0 or tolerance <= 0:
        raise ValueError("invalid stopping parameters")
    point = [float(start[0]), float(start[1])]
    history = [(0, point[0], point[1], objective(point), _norm(gradient(point)))]
    for iteration in range(1, max_iterations + 1):
        grad = gradient(point)
        if _norm(grad) <= tolerance:
            break
        direction = [-component for component in grad]
        step = armijo_backtracking(objective, gradient, point, direction)
        point = add_scaled(point, direction, step)
        grad_norm = _norm(gradient(point))
        history.append((iteration, point[0], point[1], objective(point), grad_norm))
        if grad_norm <= tolerance:
            break
    return history


def _norm(vector):
    return sum(value * value for value in vector) ** 0.5
