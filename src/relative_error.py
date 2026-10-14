"""Calculate absolute and relative numerical error."""

def absolute_error(approximation, reference):
    return abs(approximation - reference)

def relative_error(approximation, reference):
    if reference == 0:
        raise ValueError('reference value must be non-zero')
    return abs(approximation - reference) / abs(reference)
