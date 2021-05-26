from PIL import Image, ImageFilter
import numpy as np
from helper import hist, sp_noise # my lib for plot hist and add noisy
from itertools import repeat
import cv2
def median_filter(image, kernel):
    image = np.array(image, dtype=np.uint8)
    output_img = np.copy(image)
    M,N = kernel.shape[0], kernel.shape[1]
    kernel = kernel.flatten()
    for i in range(image.shape[0]-M+1):
        for j in range(image.shape[1]-N+1):
            temp_rgb = image[i:i+M,j:j+N,:]
            for k in range(image.shape[2]):
                list = []
                tmp = temp_rgb[:,:,k].flatten()
                for t in range(len(tmp)):
                    list.extend(repeat(tmp[t], kernel[t]))
                output_img[i,j,k] = np.sort(list, axis=None)[len(list)//2]
    return output_img

def median_filter_rang(image, kernel, rang):
    image = np.array(image, dtype=np.uint8)
    output_img = np.copy(image)
    M,N = kernel.shape[0], kernel.shape[1]
    kernel = kernel.flatten()
    for i in range(image.shape[0]-M+1):
        for j in range(image.shape[1]-N+1):
            temp_rgb = image[i:i+M,j:j+N,:]
            for k in range(image.shape[2]):
                list = []
                tmp = temp_rgb[:,:,k].flatten()
                for t in range(len(tmp)):
                    list.extend(repeat(tmp[t], kernel[t]))
                output_img[i,j,k] = np.sort(list, axis=None)[rang]
    return output_img
