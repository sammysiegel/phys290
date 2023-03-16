import numpy as np
from scipy.special import j0

def rho(x, y, z):
    """Density as a function of position."""
    return 4 + x**3 + 3*y*j0(z)

def integrand_M(x, y, z):
    """Integrand for the mass integral."""
    return rho(x, y, z)

def integrand_Ix(x, y, z):
    """Integrand for the x moment of inertia integral."""
    return rho(x, y, z) * x

def integrand_Iy(x, y, z):
    """Integrand for the y moment of inertia integral."""
    return rho(x, y, z) * y

def integrand_Iz(x, y, z):
    """Integrand for the z moment of inertia integral."""
    return rho(x, y, z) * z

def Monte_Carlo_integrate(integrand, xmin, xmax, ymin, ymax, zmin, zmax, N):
    '''Monte Carlo integration of a function of three variables.
    Parameters
    ----------
    integrand : function
        The function to integrate.
    xmin, xmax : float
        The limits of integration in the x direction.
    ymin, ymax : float
        The limits of integration in the y direction.
    zmin, zmax : float
        The limits of integration in the z direction.
    N : int
        The number of random points to use.
    '''
    # Generate N random points in the box.
    x = np.random.uniform(xmin, xmax, N)
    y = np.random.uniform(ymin, ymax, N)
    z = np.random.uniform(zmin, zmax, N)
    # Evaluate the integrand at each point.
    integrand_values = integrand(x, y, z)
    # Compute the volume of the box.
    V = (xmax - xmin) * (ymax - ymin) * (zmax - zmin)
    # Compute the integral.
    integral = V * np.mean(integrand_values)
    return integral

M = Monte_Carlo_integrate(integrand_M, -1, 1, -1, 1, -1, 1, 1000000)
Ix = Monte_Carlo_integrate(integrand_Ix, -1, 1, -1, 1, -1, 1, 1000000)
Iy = Monte_Carlo_integrate(integrand_Iy, -1, 1, -1, 1, -1, 1, 1000000)
Iz = Monte_Carlo_integrate(integrand_Iz, -1, 1, -1, 1, -1, 1, 1000000)

CM_x = Ix / M
CM_y = Iy / M
CM_z = Iz / M

print("The total mass is {0:.3f} and the center of mass is at ({1:.3f}, {2:.3f}, {3:.3f})".format(M, CM_x, CM_y, CM_z))