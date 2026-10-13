"""Find a root of a continuous function on a sign-changing interval."""


def root(function, left, right, tolerance=1e-8, max_iterations=1000):
    if tolerance <= 0 or max_iterations <= 0 or left >= right:
        raise ValueError("invalid interval, tolerance, or iteration limit")
    f_left, f_right = function(left), function(right)
    if f_left == 0:
        return left
    if f_right == 0:
        return right
    if f_left * f_right > 0:
        raise ValueError("function values must have opposite signs at interval ends")
    for _ in range(max_iterations):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_middle == 0 or right - left <= tolerance:
            return middle
        if f_left * f_middle < 0:
            right = middle
        else:
            left, f_left = middle, f_middle
    return (left + right) / 2
