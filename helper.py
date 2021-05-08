import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

def hist(img: np.ndarray, x='brightness', y='count pixel', title='image hist'):
    """
    The function show hist plot
    :params img input your img in RGB 
    :type img PIL.Image.Image
    """
    img = np.array(img)
    plt.hist(img.ravel(), bins=range(257))
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()

def sp_noise(image: Image.Image, prob: float)->Image.Image:
    """
    Add salt and pepper noise to image
    prob: Probability of the noise
    """
    image = np.array(image, np.uint8)
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return Image.fromarray(output)

if __name__ == "__main__":
	pass
