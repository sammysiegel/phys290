import numpy as np
import matplotlib.pyplot as plt

def user_input():
    # Get the user to input the number of links and the flexibility parameter
    n_links = int(input("Enter the number of links: "))
    flexibility = float(input("Enter the flexibility parameter: "))
    return n_links, flexibility

def build_polymer(n_links, flexibility):
    '''Build a polymer of n_links links with specified flexibility, finding the angle of each link 
    by drawing from a Gaussian distribution with mean 0 and standard deviation flexibility
    --- Inputs ---
    n_links: number of links in the polymer
    flexibility: standard deviation of the Gaussian distribution from which the angles are drawn
    --- Outputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each joint in the polymer
    '''
    # Initialize the array of coordinates
    coords = np.zeros((n_links+1, 2))
    # Find the angle of each link by drawing from a Gaussian distribution
    theta_relative = np.random.normal(0, flexibility, n_links)
    # Find the angle of each link relative to the x-axis
    theta_absolute = np.cumsum(theta_relative)
    # Find the x,y coordinates of each joint in the polymer (excluding the first joint, which is at the origin)
    coords[1:,0] = np.cumsum(np.cos(theta_absolute))
    coords[1:,1] = np.cumsum(np.sin(theta_absolute))
    return coords

def plot_polymer(coords, flexibility, start_end=False):
    '''Plot the polymer as a line connecting the joints
    --- Inputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each joint in the polymer
    flexibility: standard deviation of the Gaussian distribution from which the angles are drawn
    start_end: if True, plot a dashed line connecting the first and last joints
    --- Outputs ---
    None
    '''
    plt.figure(figsize=(8,8))
    plt.plot(coords[:,0], coords[:,1])

    plt.xlabel("x")
    plt.ylabel("y")
    x_range = np.max(coords[:,0]) - np.min(coords[:,0])
    y_range = np.max(coords[:,1]) - np.min(coords[:,1])
    plt.xlim(np.min(coords[:,0]-.1*x_range), np.max(coords[:,0])+.1*x_range)
    plt.ylim(np.min(coords[:,1])-.1*y_range, np.max(coords[:,1])+.1*y_range)
    plt.title("Polymer with {} links and flexibility = {}".format(len(coords)-1, flexibility))

    if start_end:
        plt.plot([coords[0,0], coords[-1,0]], [coords[0,1], coords[-1,1]], linestyle='--')
        distance = polymer_length(coords)
        plt.text(np.min(coords[:,0])-.05*x_range, np.max(coords[:,1])+.05*y_range, "Length = {:.2f}".format(distance))
    plt.show()

def polymer_length(coords):
    '''Calculate the length of the polymer
    --- Inputs ---
    coords: array of shape (n_links+1, 2) containing the x,y coordinates of each joint in the polymer
    --- Outputs ---
    length: length of the polymer
    '''
    distances = np.sqrt((coords[0, 0] - coords[-1, 0])**2 + (coords[0, 1] - coords[-1, 1])**2)
    return distances

def typical_length(n_links, flexibility, iterations=1000):
    '''Calculate the typical length of a polymer with n_links links and specified flexibility by averaging over iterations polymers
    --- Inputs ---
    n_links: number of links in the polymer
    flexibility: standard deviation of the Gaussian distribution from which the angles are drawn
    iterations: number of polymers to average over
    --- Outputs ---
    length: typical length of the polymer
    '''
    lengths = []
    for i in range(iterations):
        coords = build_polymer(n_links, flexibility)
        lengths.append(polymer_length(coords))
    return np.mean(lengths)

def plot_length_vs_flexibility(n_links, flex_min=0.01, flex_max=2*np.pi, n_flex=100):
    '''Plot the typical length of a polymer as a function of flexibility
    --- Inputs ---
    n_links: number of links in the polymer
    flex_min: minimum flexibility to consider
    flex_max: maximum flexibility to consider
    n_flex: number of flexibility values to consider
    --- Outputs ---
    None
    '''
    flexibilities = np.linspace(flex_min, flex_max, n_flex)
    lengths = []
    for flexibility in flexibilities:
        lengths.append(typical_length(n_links, flexibility))
    plt.figure(figsize=(8,8))
    plt.plot(flexibilities, lengths)
    plt.xlabel("Flexibility")
    plt.ylabel("Typical length")
    plt.title("Typical length of polymer with {} links".format(n_links))
    plt.show()

def main():
    n_links, flexibility = user_input()
    coords = build_polymer(n_links, flexibility)
    plot_polymer(coords, flexibility, start_end=True)
    plot_length_vs_flexibility(n_links)

main()