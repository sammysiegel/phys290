import numpy as np
import matplotlib.pyplot as plt

n_steps = 40
b = 10
theta_0 = 110 * np.pi / 180
theta_sigma = 17 * np.pi / 180

def random_walk(n_steps, theta_0, theta_sigma):
    '''Build a river of n_steps by a random walk at angles drawn from a Gaussian distribution
    with mean theta_0 and standard deviation theta_sigma (code adapted from RigidPolymer.py)
    --- Inputs ---
    n_steps: number of steps in the random walk
    theta_0: mean of the Gaussian distribution from which the angles are drawn
    theta_sigma: standard deviation of the Gaussian distribution from which the angles are drawn
    --- Outputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each point in the random walk
    '''
    # Initialize the array of coordinates
    coords = np.zeros((n_steps+1, 2))
    # Find the angle of each step by drawing from a Gaussian distribution
    theta_relative = np.random.normal(0, theta_sigma, n_steps)
    # Find the angle of each step relative to the x-axis
    theta_absolute = np.cumsum(theta_relative)
    # Shift the angles so that the first step is at theta_0
    theta_absolute = theta_0 - theta_absolute[0] + theta_absolute
    # Find the x,y coordinates of each step in the random walk (excluding the first step, which is at the origin)
    coords[1:,0] = np.cumsum(np.cos(theta_absolute))
    coords[1:,1] = np.cumsum(np.sin(theta_absolute))
    return coords

def iterate_random_walk(n_steps, b, theta_0, theta_sigma, n_iters, verbose=True):
    '''Iterate the random walk n_iters times, save the walks that are within one unit of the point (b,0),
    and return the average such random walk
    --- Inputs ---
    n_steps: number of steps in the random walk
    b: the x distance from the origin at which the random walk should end
    theta_0: mean of the Gaussian distribution from which the angles are drawn
    theta_sigma: standard deviation of the Gaussian distribution from which the angles are drawn
    n_iters: number of times to iterate the random walk
    verbose: if True, print the current number of iterations after every 1000 iterations
    --- Outputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each point in the average random walk that ends at (b,0)
    '''
    # Initialize the array of successful random walks
    successful_walks = np.zeros((0, n_steps+1, 2))
    # Iterate the random walk n_iters times
    for i in range(n_iters):
        # If verbose, print the current number of iterations after every 1000 iterations
        if verbose and i % 1000 == 0:
            print(i)
        # Find the random walk
        walk = random_walk(n_steps, theta_0, theta_sigma)
        # If the random walk ends within one unit of the point (b,0), add it to the array of successful random walks
        if np.linalg.norm(walk[-1] - np.array([b, 0])) < 1:
            successful_walks = np.append(successful_walks, np.array([walk]), axis=0)
    # Return the average of the successful random walks, averaging along the column axis
    print('Number of successful walks: {}'.format(successful_walks.shape[0]))
    return np.mean(successful_walks, axis=0), successful_walks

def plot_random_walk(coords):
    '''Plot the random walk
    --- Inputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each point in the random walk
    '''
    # Plot the random walk
    plt.plot(coords[:,0], coords[:,1])
    # Set the x and y labels
    plt.xlabel('x')
    plt.ylabel('y')
    # Set the x and y limits
    x_range = np.max(coords[:,0]) - np.min(coords[:,0])
    y_range = np.max(coords[:,1]) - np.min(coords[:,1])
    plt.xlim(np.min(coords[:,0]) - 0.1 * x_range, np.max(coords[:,0]) + 0.1 * x_range)
    plt.ylim(np.min(coords[:,1]) - 0.1 * y_range, np.max(coords[:,1]) + 0.1 * y_range)
    plt.show()

def plot_suceessful_walks(successful_walks):
    '''Plot the successful random walks, along with the average random walk
    --- Inputs ---
    successful_walks: array of shape (n_successes, n_steps+1, 2) containing the x,y coordinates of each point in each successful random walk
    '''
    average_walk = np.mean(successful_walks, axis=0)
    plt.figure(figsize=(8,8))
    # Plot the successful random walks
    for walk in successful_walks:
        plt.plot(walk[:,0], walk[:,1], color='blue', alpha=0.25)
    # Plot the average random walk
    plt.plot(average_walk[:,0], average_walk[:,1], color='red')
    # Set the x and y labels
    plt.xlabel('x')
    plt.ylabel('y')
    # Set the x and y limits
    x_range = np.max(successful_walks[:,:,0]) - np.min(successful_walks[:,:,0])
    y_range = np.max(successful_walks[:,:,1]) - np.min(successful_walks[:,:,1])
    plt.xlim(np.min(successful_walks[:,:,0]) - 0.1 * x_range, np.max(successful_walks[:,:,0]) + 0.1 * x_range)
    plt.ylim(np.min(successful_walks[:,:,1]) - 0.1 * y_range, np.max(successful_walks[:,:,1]) + 0.1 * y_range)
    plt.show()

def main():
    # Find the average random walk that ends at (b,0)
    average_walk, successful_walks = iterate_random_walk(n_steps, b, theta_0, theta_sigma, 1000000)
    # Plot the random walk
    plot_suceessful_walks(successful_walks)

main()