"""Linear interpolation with explicit domain validation."""

def interpolate(x0, y0, x1, y1, x):
    if x0 == x1:
        raise ValueError('x0 and x1 must differ')
    t = (x - x0) / (x1 - x0)
    return y0 + t * (y1 - y0)
