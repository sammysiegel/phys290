from matplotlib.image import imread
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist
Im = imread("/Users/ssiegel/Library/CloudStorage/Box-Box/2023/phys290/Problem Sets/PS7/Icebergs.jpg")

Nx, Ny, Nchannels = Im.shape

#Convert to 2D array
Im2 = Im.reshape(Nx*Ny, Nchannels)

# number of groups for k-means clustering
N_groups = 32

N_points = Im2.shape[0]

# initialize the group centers
color_centers = np.random.uniform(0,255,(N_groups,3))

# initialize the group assignments
assignments = np.zeros(N_points, dtype=int)

# initialize the distance array
distances = np.zeros((N_points, N_groups))

# iterate 20 times
for iter in range(20):
    print('iteration', iter)
    # calculate the distance between each point and each group center using the scipy function cdist
    distances = cdist(Im2, color_centers, metric='euclidean')
    # find the index of the closest group center for each point
    assignments = np.argmin(distances, axis=1)

    # update the group centers by taking the mean of the points assigned to each group
    for i in range(N_groups):
        if np.sum(assignments==i) == 0:
            color_centers[i,:] = np.random.uniform(0,255,3)
        else:
            color_centers[i,:] = np.mean(Im2[assignments==i,:], axis=0)

# assign each point to the closest group center
Result = np.zeros_like(Im2)
distances = cdist(Im2, color_centers, metric='euclidean')
assignments = np.argmin(distances, axis=1)
for i in range(N_groups):
    Result[assignments==i,:] = color_centers[i,:]

# reshape the result to the original image shape
Result = Result.reshape(Nx,Ny,Nchannels)

# plot the original image and the compressed image
fig, ax = plt.subplots(1,2, figsize=(10,5), dpi=100)
ax[0].imshow(Im)
ax[0].set_title('Original')
ax[1].imshow(Result)
ax[1].set_title('Compressed')
plt.savefig('/Users/ssiegel/Library/CloudStorage/Box-Box/2023/phys290/Problem Sets/PS7/IcebergsCompressed.png')
plt.show()
