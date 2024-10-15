import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Test File for Fourier Transform
# Using MSE instead of Energy

def get_image_difference(path1, path2):
    image1_path = path1
    image2_path = path2

    # read images to array
    image1 = mpimg.imread(image1_path)
    image2 = mpimg.imread(image2_path)

    # make greyscale
    image1 = np.mean(image1, axis=2)
    image2 = np.mean(image2, axis=2)

    # generate fourier transform of images
    fft1 = np.fft.fft2(image1)
    fft2 = np.fft.fft2(image2)

    # calculate the difference in magnitude of the two tranforms
    magnitude_difference = np.abs(fft1) - np.abs(fft2)

    # calculate the difference in phase
    # maybe for texture analysis?
    phase_difference = np.angle(fft1) - np.angle(fft2)

    # Mean Squared Error
    mse = np.mean(np.square(magnitude_difference))
    print(mse)
    input()

if __name__ == "__main__":
    get_image_difference('./Images/Image1.png', './Images/Image2.png')
