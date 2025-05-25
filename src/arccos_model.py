import math

def arccos_series(x, eps=1e-10):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a numeric type")
    if math.isnan(x) or math.isinf(x):
        raise ValueError("x must be a finite number")
    if x < -1 or x > 1:
        raise ValueError("x must be in [-1, 1]")

    if x == 1:
        return 0.0
    if x == -1:
        return math.pi

    sum_series = 0.0
    n = 0
    while True:
        coeff = math.factorial(2*n) / ((4**n) * (math.factorial(n)**2) * (2*n + 1))
        term = coeff * (x**(2*n + 1))
        if abs(term) < eps:
            break
        sum_series += term
        n += 1

    return math.pi/2 - sum_series