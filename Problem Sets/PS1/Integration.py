import numpy as np
import matplotlib.pyplot as plt

def trapezoid(f, a, b, n):
    """Approximate the integral of f from a to b by the trapezoid rule.
    f: function to integrate
    a: lower limit of integration
    b: upper limit of integration
    n: number of subintervals to use
    """
    Integral = 0
    x = np.linspace(a, b, n+1)
    dx = x[1] - x[0]
    for i in range(1, n+1):
        Integral += .5*(f(x[i]) + f(x[i-1]))*dx
    return Integral

def rectangle(f, a, b, n):
    """Approximate the integral of f from a to b by the rectangle rule.
    f: function to integrate
    a: lower limit of integration
    b: upper limit of integration
    n: number of subintervals to use
    """
    Integral = 0
    x = np.linspace(a, b, n+1)
    dx = x[1] - x[0]
    for i in range(0, n):
        Integral += f(x[i])*dx
    return Integral

# Print the error of the trapezoid and rectangle rules calculated using 100 subintervals relative to the error calculated using 200 subintervals.
print('Trapezoid Relative Error:', (1-trapezoid(np.sin, 0, np.pi/2, 100))/(1-trapezoid(np.sin, 0, np.pi/2, 200)))
print('Rectangle Relative Error:', (1-rectangle(np.sin, 0, np.pi/2, 100))/(1-rectangle(np.sin, 0, np.pi/2, 200)))

# Plot the error of the trapezoid and rectangle rules as a function of the number of subintervals used.
# We can compare this error to 1/N^2 and 1/N.
N = np.linspace(10, 100, 100).astype(int)
trap_err = []
rect_err = []
for n in N:
    trap_err.append(abs(trapezoid(np.sin, 0, np.pi/2, n) - 1))
    rect_err.append(abs(rectangle(np.sin, 0, np.pi/2, n) - 1))

plt.plot(N, trap_err, label='Trapezoid')
plt.plot(N, rect_err, label='Rectangle')
plt.plot(N, (1/N**2)*(trap_err[0]/(1/N[0]**2)), label='1/N^2', linestyle='--', color = 'magenta')
plt.plot(N, (1/N)*(rect_err[0]/(1/N[0])), label='1/N', linestyle='--', color='cyan')
plt.legend()
plt.xlabel('N')
plt.ylabel('Error')
plt.show()