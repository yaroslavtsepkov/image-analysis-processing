import matplotlib.pyplot as plt
import numpy as np
import random

def sp_noise(image:np.ndarray, prob: float)->np.ndarray:
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
    return output[i][j]

if __name__ == "__main__":
	pass
