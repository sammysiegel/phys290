from matplotlib.image import imread
from matplotlib import pyplot as plt
import numpy as np

einstein = imread("/Users/ssiegel/Library/CloudStorage/Box-Box/2023/phys290/Problem Sets/PS8/Einstein.png")
curie = imread("/Users/ssiegel/Library/CloudStorage/Box-Box/2023/phys290/Problem Sets/PS8/Curie.png")[:,:,0]

def image_fft(Image, shift=False):
    # take the fourier transform of the image
    image_spectrum = (np.fft.fft2(Image))
    if shift:
        image_spectrum = np.fft.fftshift(image_spectrum)
    fx = np.fft.fftfreq(Image.shape[1])
    fy = np.fft.fftfreq(Image.shape[0])
    return image_spectrum, fx, fy

def image_ifft(Image):
    # take the inverse fourier transform of the image
    image_spectrum = np.fft.ifft2(Image).real
    return image_spectrum

def normalize_image(Image):
    # normalize the image
    Image = Image - np.min(Image)
    Image = Image/np.max(Image)
    return Image

def power_spectrum(Image):
    # calculate the power spectrum of the image
    Image = (np.abs(Image))**2
    return 10*np.log(Image)

def display_spectrum(Image):
    to_display = power_spectrum(Image/np.max(Image))
    plt.imshow(to_display, cmap='gray')
    plt.colorbar()
    plt.show()

def LogisticFn(x, x0, w):
    return 1./(1.+np.exp(-(x-x0)/w))

def filter(Image, threshold=0.04, high_pass=True):
    # create a high pass filter/low pass filter
    Image, fx, fy = image_fft(Image)
    kx, ky = np.meshgrid(fx, fy)
    Kmag = np.sqrt(kx**2 + ky**2)
    print(Kmag.shape)
    cutoff = threshold*np.max(Kmag)
    if high_pass:
        Image = Image*(LogisticFn(Kmag, cutoff, 0.01))
    else:
        Image = Image*(1-LogisticFn(Kmag, cutoff, 0.01))
    Image = image_ifft(Image)
    Image = normalize_image(Image)
    return Image

filtered_einstein = filter(einstein)
filtered_curie = filter(curie, high_pass=False)

# I ended up using a 60/40 split of the two images because I thought it made it easier to see Einstein.
merged_image = .6*filtered_einstein + .4*filtered_curie

fig, ax = plt.subplots(1,3, figsize=(15,5), dpi=100)
ax[0].imshow(einstein, cmap='gray')
ax[0].set_title('Original Einstein')
ax[1].imshow(curie, cmap='gray')
ax[1].set_title('Original Curie')
ax[2].imshow(merged_image, cmap='gray')
ax[2].set_title('Merged Image')
plt.savefig('/Users/ssiegel/Library/CloudStorage/Box-Box/2023/phys290/Problem Sets/PS8/FilterIllusion.png')
plt.show()







