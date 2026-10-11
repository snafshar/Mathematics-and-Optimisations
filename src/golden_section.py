"""Golden-section search for a unimodal scalar objective."""


def minimize(function, left, right, tolerance=1e-8):
    if right <= left or tolerance <= 0:
        raise ValueError("invalid interval or tolerance")
    phi = (1 + 5 ** 0.5) / 2
    inv = 1 / phi
    x1 = right - (right - left) * inv
    x2 = left + (right - left) * inv
    f1, f2 = function(x1), function(x2)
    while right - left > tolerance:
        if f1 < f2:
            right, x2, f2 = x2, x1, f1
            x1 = right - (right - left) * inv
            f1 = function(x1)
        else:
            left, x1, f1 = x1, x2, f2
            x2 = left + (right - left) * inv
            f2 = function(x2)
    return (left + right) / 2
