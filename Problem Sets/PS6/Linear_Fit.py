import numpy as np
import matplotlib.pyplot as plt

# Define the function to compute pi
def Pi(N):
    x = np.random.uniform(0, 1, N)
    return np.mean(4. * np.sqrt(1. - x**2))

def residuals(p, k, x, y):
    '''Compute the residuals of a linear fit.
    Parameters
    ----------
    p : float
        The slope of the line.
    k : float
        The y-intercept of the line.
    x : array of float
        The x-coordinates of the data.
    y : array of float
        The y-coordinates of the data.
    Returns
    -------
    residuals : array of float
        The difference between the data and the fit.'''
    return y - (p*x + k)

# Define the range of N - I'm sampling evenly in log space from roughly N = 10 to N = 10000 as 
# sampling in linear space gives a fit dominated by the first few points
N_list = np.linspace(2.3, 9.21, 1000)
N_list = np.exp(N_list).astype(int)
std_list = []

# Compute the standard deviation of pi for 100 trials for each N
for N in N_list:
    pi_list = np.zeros(100)
    for i in range(100):
        pi_list[i] = Pi(N)
    std_list.append(np.std(pi_list))

std_list = np.array(std_list)

# Take the log of N and the standard deviation
x = np.log(N_list)
y = np.log(std_list)

p_hat = (np.mean(x*y) - np.mean(x) * np.mean(y))/((np.mean(x**2)) - np.mean(x)**2)
k_hat = np.mean(y) - p_hat * np.mean(x)
err = residuals(p_hat, k_hat, x, y)
p_err = np.sqrt((1./(len(x)-2)) * np.sum(err**2) / np.sum((x - np.mean(x))**2))
k_err = p_err * np.sqrt(np.mean(x**2))

plt.figure(figsize = (10, 8))
plt.scatter(x, y, label = "Data", color = "blue", s=3)
plt.plot(x, p_hat*x + k_hat, label = "$\hat{y} = (%.3f \pm %.3f) x + (%.3f \pm %.3f)$"%(p_hat, p_err, k_hat, k_err), color = "red", linestyle = "--")
plt.fill_between(x, (p_hat +2*p_err)*x + (k_hat + 2*k_err), (p_hat -2*p_err)*x + (k_hat - 2*k_err), color = "red", alpha = 0.5, label = "95% Confidence Interval")
plt.xlabel("log N")
plt.ylabel("log $\sigma$")
plt.legend()
plt.title("Linear Fit of $\sigma$ vs. log N")
plt.show()
    
