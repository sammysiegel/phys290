import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#define the real and complex grids
x1d = np.linspace(-2, 2, 1000)
y1d = np.linspace(-2, 2, 1000)
x, y = np.meshgrid(x1d, y1d)
z = x + 1j * y

# define the roots of z^3 - 1
r0 = 1
r1 = -.5 + 1j * np.sqrt(3) / 2
r2 = -.5 - 1j * np.sqrt(3) / 2

# I'm going to keep track of how many iterations it takes to reach a tolerance (1e-12 in this case)
iterations = np.zeros_like(z, dtype=int)

# use the Newton-Raphson method to find the roots of z^3 - 1 for each point in the complex grid
for _ in range(30):
    # identify the points that have not yet reached tolerance
    idx = np.where((np.abs(z - r0) > 1e-12) & (np.abs(z - r1) > 1e-12) & (np.abs(z - r2) > 1e-12))
    # iterate the points that have not yet reached tolerance
    z[idx] = 2/3 * z[idx] + 1/(3 * z[idx]**2)
    # increment the iteration count for the points that have not yet reached tolerance
    iterations[idx] += 1

# plot the results
# I'm going to give the color of each point by specifying HSV values: hue will be the phase of the point, the saturation will be 1, and the value will be the number of iterations it took to reach tolerance
zphase = np.angle(z)

# Establish the normalization for the hue and value. Note that I'm using the negative of the iteration count so that the points that took the fewest iterations will be the brightest
h_norm = mpl.colors.Normalize(vmin=np.min(zphase), vmax=np.max(zphase))
v_norm = mpl.colors.Normalize(vmin=-np.max(iterations), vmax=-np.min(iterations))

# Create the HSV colors
HSV_colors = np.zeros((1000, 1000, 3))
HSV_colors[:, :, 0] = h_norm(zphase)
HSV_colors[:, :, 1] = 1
HSV_colors[:, :, 2] = v_norm(-iterations)

# Convert the HSV colors to RGB for plotting
RGB_colors = mpl.colors.hsv_to_rgb(HSV_colors)

plt.figure(figsize=(8, 8))
plt.imshow(RGB_colors, extent=(-2,2,-2,2))
plt.show()