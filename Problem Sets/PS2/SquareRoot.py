import numpy as np
import matplotlib.pyplot as plt

n = 2.

def FA(x):
    return .2*x+.8*n/x

def FB(x):
    return .5*(x+n/x)

def FC(x):
    Num = x*(x**2+3*n)
    Den = 3*x**2+n
    return Num/Den

def iterate(f, x0, tol=1e-12, N=100):
    """Iterate the function f n times starting at x0.
    f: function to iterate
    x0: starting value
    n: number of iterations
    Returns: the value of f^n(x0)
    """
    x_prev = 0
    for i in range(N):
        x_prev = x0
        x0 = f(x0)
        if abs(x0 - x_prev) < tol:
            print('x = ', x0, '+/-', abs(x0 - x_prev), 'after', i, 'iterations')
            break
    else:
        print('x = ', x0, '+/-', abs(x0 - x_prev), 'after', i, 'iterations')


# run the iterate function for FA, FB, and FC
print('Iterating FA...')
iterate(FA, .1)
print('Iterating FB...')
iterate(FB, .1)
print('Iterating FC...')
iterate(FC, .1)