import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0, j1

# Use a grid search to find the first 20 roots of the Bessel function J0(x)
rough_roots = []
x0 = 0.0
while len(rough_roots) < 20:
    x1 = x0 + 0.1
    if j0(x0) * j0(x1) < 0:
        rough_roots.append(x1)
    x0 = x1

refined_roots = np.array(rough_roots)

# Use the Newton-Raphson method to refine the roots
for _ in range(10):
    refined_roots += j0(refined_roots) / j1(refined_roots)

print('The first 20 roots of the Bessel function J0(x) are:', refined_roots)

# Plot the Bessel function J0(x) and the roots
x = np.linspace(0, 65, 1000)
plt.figure(figsize=(8, 6))
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.plot(x, j0(x), label='J0(x)')
plt.scatter(refined_roots, j0(refined_roots), label='refined roots', marker='o', color='green', s=30)
plt.scatter(rough_roots, j0(rough_roots), label='rough roots', marker='x', color='red', s=20)
plt.legend()
plt.xlabel('x')
plt.ylabel('J0(x)')
plt.show()