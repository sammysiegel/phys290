### Logistic Map Bifurcation Diagram
### To create the diagram, I chose to use the imshow method. I made use of the convenient np.histogram() function bin the results of iteration for each a, returning an area with count values for each x bin.
### These count values were then the basis for each pixel in the image array. 

import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def LogMap(x, a):
    return a*x*(1-x)

# Define the number of bins
Na = 5000
Nx = 1000

# Define the range of a and x
a = np.linspace(0, 4, Na)
x = np.linspace(0, 1, Nx)


img_array = np.zeros((Nx-1, Na))

for idx in range(Na):
    iterant = np.copy(x)
    for _ in range(1000):
        iterant = LogMap(iterant, a[idx])

    # after iterating, we bin the results by x value, getting the number of counts for each x value
    iterant = np.histogram(iterant, bins=x, range=(0,1))[0]

    # the number of counts becomes the appropriate column in the image array
    img_array[:, idx] = iterant

# Take the arcsinh of all the counts to make the smaller values more visible, then normalize the array
img_array = np.arcsinh(img_array)
img_array = img_array/np.max(img_array)

plt.figure(figsize=(16, 10))
plt.imshow(img_array, cmap='Reds', extent=[0, 4, 0, 1], aspect='auto', origin='lower')
plt.xlabel('a value')
plt.ylabel('x after many iterations')
plt.title('Logistic Map Bifurcation Diagram')
plt.colorbar(label='Arcsinh Number of Counts (Normalized)')

# removing the black border around the image to made the edges more visible
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.savefig("BifurcationDiagram.png", dpi=1000)