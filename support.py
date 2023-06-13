import numpy as np
import os
import shutil

def rgb2gray(image):
    dtype = image.dtype
    gray = np.dot(image[...,:3], [0.299, 0.587, 0.114])
    return gray.astype(dtype)

def rmdir(directory):
    directory = os.path.abspath(directory)
    if os.path.exists(directory): 
        shutil.rmtree(directory)  

def mkdir(directory):
    directory = os.path.abspath(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
        