# Problem 1: Calculate pi using the bisection method.
# The plan: calculate the root of $f(x) = sin(x) using the bisection algorithm in the interval [3, 4]. As we know, sin(pi) = 0, so we will be calculating pi.

import numpy as np

def bisection(f, a, b, tol):
    """Approximate the root of f in the interval [a, b] using the bisection method.
    f: function to find the root of
    a: lower limit of the interval
    b: upper limit of the interval
    tol: tolerance for the error (once error is less than tol, the function stops and returns the root)
    Returns: the root of f in the interval [a, b]
    """
    # Check that the function has opposite signs at the endpoints of the interval.
    if f(a)*f(b) >= 0:
        raise ValueError('f(a) and f(b) must have opposite signs.')
    for _ in range(100):
        # Calculate the midpoint of the interval.
        c = (a + b)/2
        # if the midpoint is the root, we are done.
        if f(c) == 0:
            # we're not gonna need this next line of code...
            print('pi =', c, '+/- 0')
            return c, 0
        # Determine the new interval.
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        # Calculate the error.
        err = abs(b - a)/2
        print('pi =', c, '+/-', err)
        if err < tol:
            return c, err
    else:
        print('pi =', c, '+/-', err)
        return c, err

# run the function
pi, err = bisection(np.sin, 3, 4, 1e-13)
